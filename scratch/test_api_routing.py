import os
import django
from django.urls import resolve, reverse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resume_project.settings')
django.setup()

try:
    url = reverse('resume-list')
    print(f"API List URL found: {url}")
    match = resolve('/api/v1/resumes/')
    print(f"API List Path resolves to: {match.func}")
except Exception as e:
    print(f"Error: {e}")
