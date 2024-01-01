# Create your views here.
from django.shortcuts import render
from .models import Education, Experience
from django.http import JsonResponse
from .serializers import ExperienceSerializer, EducationSerializer

def education_list(request):
    educations = Education.objects.all()
    return render(request, 'resume/education_list.html', {'educations': educations})

def experience_list(request):
    experiences = Experience.objects.all()
    return render(request, 'resume/experience_list.html', {'experiences': experiences})


def experience_list_json(request):
    experiences = Experience.objects.all()
    serializer = ExperienceSerializer(experiences, many=True)
    return JsonResponse(serializer.data, safe=False)

def education_list_json(request):
    education = Education.objects.all()
    serializer = EducationSerializer(education, many=True)
    return JsonResponse(serializer.data, safe=False)