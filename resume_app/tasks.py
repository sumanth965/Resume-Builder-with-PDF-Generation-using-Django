import os
from celery import shared_task
from django.conf import settings
from django.template.loader import render_to_string
import uuid

@shared_task
def generate_pdf_task(resume_id, context):
    """
    Generate a high-fidelity PDF using WeasyPrint with robust error handling for missing system dependencies.
    """
    try:
        from weasyprint import HTML
        
        # 1. Render HTML
        html_string = render_to_string('resume_print.html', context)
        
        # 2. Define output path
        filename = f"resume_{resume_id}_{uuid.uuid4().hex[:8]}.pdf"
        relative_path = os.path.join('resumes', filename)
        absolute_path = os.path.join(settings.MEDIA_ROOT, relative_path)
        
        # 3. Ensure directory exists
        os.makedirs(os.path.dirname(absolute_path), exist_ok=True)
        
        # 4. Generate PDF
        # We wrap this call specifically because on Windows it often fails with OSError 
        # if GTK/Pango libraries are missing from the SYSTEM PATH.
        HTML(string=html_string).write_pdf(absolute_path)
        
        # 5. Return the URL
        return {
            "status": "SUCCESS",
            "resume_id": resume_id,
            "file_url": f"{settings.MEDIA_URL}{relative_path}"
        }
    except (ImportError, OSError, Exception) as e:
        return {
            "status": "FAILURE",
            "error": str(e),
            "help": "Ensure GTK+ is installed on your system to enable PDF generation."
        }
