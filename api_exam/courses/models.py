from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    id = models.CharField(max_length=10, primary_key=True)
    course = models.CharField(max_length=50)

def __str__(self):
    return self.name

class Teacher(models.Model):
    teacher_name=models.CharField(max_length=100)
    teacher_courses = models.CharField(max_length=50)
    teacher_course_date = models.DateTimeField("date starting")

    def __str__(self):
        return self.teacher_name


# class Student(models.Model):
