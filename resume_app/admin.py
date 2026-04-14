from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'template_name', 'created_at')
    list_filter = ('template_name', 'created_at')
    search_fields = ('name', 'email', 'programming_languages', 'tools')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email', 'phone', 'career_objective')
        }),
        ('Curated Content', {
            'fields': ('education', 'internship', 'programming_languages', 'web_frameworks', 'databases', 'tools', 'achievements', 'hobbies')
        }),
        ('System Settings', {
            'fields': ('template_name',)
        }),
    )
