from django.shortcuts import render
from rest_framework import viewsets
from .models import Course,Teacher
from .serializers import CourseSerializer
# Create your views here.

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    # queryset = Teacher.objects.all()
    serializer_class = CourseSerializer
