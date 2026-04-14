from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)

    career_objective = models.TextField(blank=True)
    education = models.TextField(blank=True)

    programming_languages = models.TextField(blank=True)
    web_frameworks = models.TextField(blank=True)
    databases = models.TextField(blank=True)
    tools = models.TextField(blank=True)

    strengths = models.TextField(blank=True)
    certificates = models.TextField(blank=True)
    extracurricular = models.TextField(blank=True)

    projects = models.TextField(blank=True)
    internship = models.TextField(blank=True)

    languages_known = models.TextField(blank=True)
    achievements = models.TextField(blank=True)
    hobbies = models.TextField(blank=True)

    def __str__(self):
        return self.name
