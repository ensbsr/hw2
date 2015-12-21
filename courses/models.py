from django.db import models
from django.shortcuts import render_to_response
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    office_details = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()

class Course(models.Model):
    student = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher)
    course_name = models.CharField(max_length=30)
    course_code = models.CharField(max_length=3)
    course_classroom = models.CharField(max_length=30)
    course_time = models.CharField(max_length=30)






