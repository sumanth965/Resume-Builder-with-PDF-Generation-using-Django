from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError

# Validators
date_validator = RegexValidator(
    regex=r'^\d{4}-\d{2}-\d{2}$',
    message="Date must be in YYYY-MM-DD format"
)
phone_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)

class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()])
    phone = models.CharField(max_length=15, blank=True, validators=[phone_validator])
    template_name = models.CharField(max_length=50, default='modern')

    career_objective = models.TextField(blank=True)
    education = models.TextField(blank=True) # Legacy

    programming_languages = models.TextField(blank=True)
    web_frameworks = models.TextField(blank=True)
    databases = models.TextField(blank=True)
    tools = models.TextField(blank=True)

    strengths = models.TextField(blank=True)
    certificates = models.TextField(blank=True)
    extracurricular = models.TextField(blank=True)

    projects = models.TextField(blank=True) # Legacy
    experience_legacy = models.TextField(blank=True) 
    internship = models.TextField(blank=True) # Legacy

    languages_known = models.TextField(blank=True)
    achievements = models.TextField(blank=True)
    hobbies = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()
        # Requirement: At least one education or experience entry is required
        # Note: In Django Admin, relations are saved AFTER the parent model, 
        # so this check might be tricky in model.clean() for new objects.
        # We'll implement it but skip if the object is new.
        if self.pk:
            if not self.education_entries.exists() and not self.experience_entries.exists():
                raise ValidationError("At least one education or experience entry is required.")

    def __str__(self):
        return f"{self.name} ({self.email})"

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='education_entries')
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    start_date = models.CharField(max_length=10, blank=True, validators=[date_validator])
    end_date = models.CharField(max_length=10, blank=True) # Can be 'Present'
    marks = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experience_entries')
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    start_date = models.CharField(max_length=10, blank=True, validators=[date_validator])
    end_date = models.CharField(max_length=10, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.role} at {self.company}"
