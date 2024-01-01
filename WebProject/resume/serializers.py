# serializers.py 
from rest_framework import serializers
from .models import Experience, Education

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'job_title', 'company', 'start_date', 'end_date', 'description']
        # Include other fields as needed


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'degree', 'institution', 'graduation_year']
        # Include other fields as needed