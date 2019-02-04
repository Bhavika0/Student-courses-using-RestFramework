
from rest_framework import serializers
from .models import Course,Teacher


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id','url' ,'name', 'course' )

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('teacher_name','teacher_courses', 'teacher_course_date')
