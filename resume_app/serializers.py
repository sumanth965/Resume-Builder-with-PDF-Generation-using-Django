from rest_framework import serializers
from .models import Resume, Education, Experience

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'institution', 'degree', 'start_date', 'end_date', 'marks']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'company', 'role', 'start_date', 'end_date', 'description']

class ResumeSerializer(serializers.ModelSerializer):
    education_entries = EducationSerializer(many=True)
    experience_entries = ExperienceSerializer(many=True)

    class Meta:
        model = Resume
        fields = [
            'id', 'name', 'email', 'phone', 
            'career_objective', 'education', 
            'programming_languages', 'web_frameworks', 
            'databases', 'tools', 'strengths', 
            'certificates', 'extracurricular', 
            'projects', 'internship', 
            'languages_known', 'achievements', 'hobbies',
            'education_entries', 'experience_entries'
        ]

    def create(self, validated_data):
        education_data = validated_data.pop('education_entries', [])
        experience_data = validated_data.pop('experience_entries', [])
        resume = Resume.objects.create(**validated_data)
        
        for edu in education_data:
            Education.objects.create(resume=resume, **edu)
        for exp in experience_data:
            Experience.objects.create(resume=resume, **exp)
            
        return resume

    def update(self, instance, validated_data):
        education_data = validated_data.pop('education_entries', None)
        experience_data = validated_data.pop('experience_entries', None)

        # Update core Resume fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update nested Education (Replace all for simplicity in v1)
        if education_data is not None:
            instance.education_entries.all().delete()
            for edu in education_data:
                Education.objects.create(resume=instance, **edu)

        # Update nested Experience (Replace all for simplicity in v1)
        if experience_data is not None:
            instance.experience_entries.all().delete()
            for exp in experience_data:
                Experience.objects.create(resume=instance, **exp)

        return instance
