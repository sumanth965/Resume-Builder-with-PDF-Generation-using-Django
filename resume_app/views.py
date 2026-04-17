from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Resume   # ✅ IMPORTANT

# Force reload - dummy comment
def create_resume(request):
    if request.method == "POST":

        # ---------- HELPERS ----------
        def split_data(field):
            if field:
                return [i.strip() for i in field.split(',') if i.strip()]
            return []

        def split_lines(field):
            return field.splitlines() if field else []

        # ---------- GET DATA ----------
        programming_languages = request.POST.get('programming_languages', '')
        web_frameworks = request.POST.get('web_frameworks', '')
        databases = request.POST.get('databases', '')
        tools = request.POST.get('tools', '')

        achievements = request.POST.get('achievements', '')
        hobbies = request.POST.get('hobbies', '')

        strengths = request.POST.get('strengths', '')
        certificates = request.POST.get('certificates', '')
        extracurricular = request.POST.get('extracurricular', '')
        languages_known = request.POST.get('languages_known', '')

        projects = request.POST.get('projects', '')
        internship = request.POST.get('internship', '')

        education = request.POST.get('education', '')

        # 🔥 ✅ SAVE TO DATABASE (ADDED HERE)
        Resume.objects.create(
            name=request.POST.get('name', ''),
            email=request.POST.get('email', ''),
            phone=request.POST.get('phone', ''),
            career_objective=request.POST.get('career_objective', ''),

            education=education,
            projects=projects,
            internship=internship,

            programming_languages=programming_languages,
            web_frameworks=web_frameworks,
            databases=databases,
            tools=tools,

            strengths=strengths,
            certificates=certificates,
            extracurricular=extracurricular,
            languages_known=languages_known,

            achievements=achievements,
            hobbies=hobbies
        )

        # ---------- EDUCATION PARSE ----------
        lines = [line.strip() for line in education.splitlines() if line.strip()]

        education_data = []
        temp = {}

        for line in lines:
            if line.startswith("College:"):
                if temp:
                    education_data.append(temp)
                    temp = {}
                temp["college"] = line.replace("College:", "").strip()

            elif line.startswith("Course:"):
                temp["course"] = line.replace("Course:", "").strip()

            elif line.startswith("Marks:"):
                temp["marks"] = line.replace("Marks:", "").strip()

            elif line.startswith("Year:"):
                temp["year"] = line.replace("Year:", "").strip()

        if temp:
            education_data.append(temp)

        # ---------- CONTEXT ----------
        context = {
            "resume": {
                "name": request.POST.get('name', ''),
                "email": request.POST.get('email', ''),
                "phone": request.POST.get('phone', ''),
                "career_objective": request.POST.get('career_objective', ''),

                "education_data": education_data,

                "projects_lines": split_lines(projects),
                "internship_lines": split_lines(internship),

                "programming_languages_list": split_data(programming_languages),
                "web_frameworks_list": split_data(web_frameworks),
                "databases_list": split_data(databases),
                "tools_list": split_data(tools),

                "achievements_list": split_data(achievements),
                "hobbies_list": split_data(hobbies),

                "strengths_list": split_data(strengths),
                "certificates_list": split_data(certificates),
                "extracurricular_lines": split_lines(extracurricular),
                "languages_known_list": split_data(languages_known),
            }
        }

        # ---------- PDF ----------
        template = get_template('resume_pdf_v2.html')
        html = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

        pisa.CreatePDF(html, dest=response)

        return response

    return render(request, "form.html")