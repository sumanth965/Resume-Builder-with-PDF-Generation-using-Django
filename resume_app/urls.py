from django.urls import path
from . import views, api

urlpatterns = [
    path('', views.resume_list, name='resume_list'),
    path('create/', views.create_resume, name='create_resume'),
    path('edit/<int:resume_id>/', views.create_resume, name='edit_resume'),
    path('htmx/education-form/', views.get_education_form, name='get_education_form'),
    path('htmx/experience-form/', views.get_experience_form, name='get_experience_form'),
    path('htmx/live-preview/', views.live_preview, name='live_preview'),
    path('export/html/<int:resume_id>/', views.export_resume_html, name='export_resume_html'),
    path('api/v1/pdf/status/<str:task_id>/', api.get_pdf_status, name='get_pdf_status'),
]