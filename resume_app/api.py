from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from celery.result import AsyncResult
from .models import Resume
from .serializers import ResumeSerializer

class ResumeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows resumes to be viewed, created, or edited.
    """
    queryset = Resume.objects.prefetch_related('education_entries', 'experience_entries').all()
    serializer_class = ResumeSerializer
    filterset_fields = ['name', 'email']
    search_fields = ['name', 'programming_languages', 'tools', 'career_objective']

@api_view(['GET'])
def get_pdf_status(request, task_id):
    """
    Check the status of a PDF generation task.
    """
    res = AsyncResult(task_id)
    return Response({
        "task_id": task_id,
        "status": res.status,
        "result": res.result if res.ready() else None
    })
