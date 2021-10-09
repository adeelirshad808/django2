from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models.base import Model


class Teacher(models.Model):
    teacher_name = models.OneToOneField(User, on_delete=models.CASCADE)
    isTeacher = models.BooleanField(default=True)

    def __str__(self):
        return str(self.teacher_name)


class Student(models.Model):
    student_name = models.OneToOneField(User,
                                        on_delete=models.CASCADE,
                                        null=True)
    student_class = models.CharField(null=True, max_length=30)
    isStudent = models.BooleanField(default=False)

    def __str__(self):
        return str(self.student_name)


# This holds all the grading and stuff for a submission of an assignment
class Submissions(models.Model):
    submitted_by = models.ForeignKey(Student,
                                     unique=False,
                                     null=False,
                                     on_delete=models.CASCADE)
    submission_file = models.FileField(null=False, unique=False)
    marks_obtained = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.submitted_by)


class Assignment(models.Model):
    assignment_creator = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    assignment_details = models.TextField(null=True)

    def __str__(self):
        return str(self.assignment_creator)
