from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Resume
from .tasks import generate_pdf_task

def resume_list(request):
    resumes = Resume.objects.all().order_by('-id')
    return render(request, 'dashboard.html', {'resumes': resumes})

def _get_resume_context(request):
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    career_objective = request.POST.get('career_objective', '')
    template_name = request.POST.get('template_name', 'modern')
    education = request.POST.get('education', '')
    internship = request.POST.get('internship', '')
    
    education_data = []
    lines = [line.strip() for line in education.splitlines() if line.strip()]
    temp = {}
    for line in lines:
        if line.startswith("College:"):
            if temp: education_data.append(temp); temp = {}
            temp["college"] = line.replace("College:", "").strip()
        elif line.startswith("Course:"): temp["course"] = line.replace("Course:", "").strip()
        elif line.startswith("Marks:"): temp["marks"] = line.replace("Marks:", "").strip()
    if temp: education_data.append(temp)

    experience_data = []
    lines = [line.strip() for line in internship.splitlines() if line.strip()]
    temp = {}
    for line in lines:
        if line.startswith("Company:"):
            if temp: experience_data.append(temp); temp = {}
            temp["company"] = line.replace("Company:", "").strip()
        elif line.startswith("Role:"): temp["role"] = line.replace("Role:", "").strip()
        elif line.startswith("Work:"): temp["work"] = line.replace("Work:", "").strip()
    if temp: experience_data.append(temp)

    return {
        "name": name, "email": email, "phone": phone, "career_objective": career_objective,
        "template_name": template_name,
        "education_list": education_data,
        "experience_list": experience_data,
        "programming_languages": request.POST.get('programming_languages', ''),
        "web_frameworks": request.POST.get('web_frameworks', ''),
        "databases": request.POST.get('databases', ''),
        "tools": request.POST.get('tools', ''),
        "achievements": request.POST.get('achievements', ''),
        "hobbies": request.POST.get('hobbies', ''),
        "education_raw": education,
        "internship_raw": internship
    }

def create_resume(request, resume_id=None):
    resume = None
    if resume_id:
        resume = get_object_or_404(Resume, id=resume_id)

    if request.method == "POST":
        context = _get_resume_context(request)
        r_id = request.POST.get('resume_id')
        if r_id:
            resume = Resume.objects.get(id=r_id)
            for key, value in context.items():
                if hasattr(resume, key) and key not in ['education_list', 'experience_list']:
                    setattr(resume, key, value)
            resume.education = context['education_raw']
            resume.internship = context['internship_raw']
            resume.save()
        else:
            resume = Resume.objects.create(
                name=context['name'], email=context['email'], phone=context['phone'], 
                career_objective=context['career_objective'],
                template_name=context['template_name'],
                education=context['education_raw'], 
                internship=context['internship_raw'],
                programming_languages=context['programming_languages'], 
                web_frameworks=context['web_frameworks'],
                databases=context['databases'], 
                tools=context['tools'], 
                achievements=context['achievements'], 
                hobbies=context['hobbies']
            )

        task_id = None
        file_url = None
        try:
            # Try Async with Celery
            task = generate_pdf_task.delay(resume.id, context)
            task_id = task.id
        except Exception:
            # Fallback to Synchronous if Redis/Celery fails
            result = generate_pdf_task(resume.id, context)
            if result.get('status') == 'SUCCESS':
                file_url = result.get('file_url')

        if request.headers.get('HX-Request'):
            return JsonResponse({"task_id": task_id, "file_url": file_url, "resume_id": resume.id})
        
        return render(request, "preparing_pdf.html", {"task_id": task_id, "file_url": file_url, "resume": resume})

    initial_data = {}
    if resume:
        initial_data = {
            'resume': resume,
            'template_name': resume.template_name,
            'education_rows': _parse_raw_to_list(resume.education, 'education'),
            'experience_rows': _parse_raw_to_list(resume.internship, 'experience')
        }
    else:
        initial_data = {'template_name': 'modern'}

    return render(request, "form.html", initial_data)

def _parse_raw_to_list(raw_text, mode):
    data = []
    if not raw_text: return data
    lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
    temp = {}
    for line in lines:
        if mode == 'education':
            if line.startswith("College:"):
                if temp: data.append(temp); temp = {}
                temp["college"] = line.replace("College:", "").strip()
            elif line.startswith("Course:"): temp["course"] = line.replace("Course:", "").strip()
            elif line.startswith("Marks:"): temp["marks"] = line.replace("Marks:", "").strip()
        else:
            if line.startswith("Company:"):
                if temp: data.append(temp); temp = {}
                temp["company"] = line.replace("Company:", "").strip()
            elif line.startswith("Role:"): temp["role"] = line.replace("Role:", "").strip()
            elif line.startswith("Work:"): temp["work"] = line.replace("Work:", "").strip()
    if temp: data.append(temp)
    return data

def export_resume_html(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    # Re-use the context parser or just manually build from object
    # For speed, I'll manually build the context
    context = {
        "name": resume.name, "email": resume.email, "phone": resume.phone,
        "career_objective": resume.career_objective, "template_name": resume.template_name,
        "education_list": _parse_raw_to_list(resume.education, 'education'),
        "experience_list": _parse_raw_to_list(resume.internship, 'experience'),
        "programming_languages": resume.programming_languages,
        "web_frameworks": resume.web_frameworks, "databases": resume.databases,
        "tools": resume.tools, "achievements": resume.achievements, "hobbies": resume.hobbies,
        "is_print": True
    }
    return render(request, 'resume_print.html', context)

def live_preview(request):
    if request.method == "POST":
        context = _get_resume_context(request)
        return render(request, 'partials/preview_pane.html', context)
    return HttpResponse("")

def get_education_form(request):
    return render(request, 'partials/education_row.html')

def get_experience_form(request):
    return render(request, 'partials/experience_row.html')
