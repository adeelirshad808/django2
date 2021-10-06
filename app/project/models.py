from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models.base import Model


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Registered account'
        verbose_name_plural = 'Registered accounts'

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    teacher_name = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    task_details = models.FileField()

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return self.teacher_name


class Assignment(models.Model):
    assignment_crator = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    upload_assignment = models.FileField(null=True)
    marks_obtained = models.FloatField(default=0.0)

    class Meta:
        verbose_name = 'Assignment'
        verbose_name_plural = 'Assignments'


class Student(models.Model):
    student_name = models.OneToOneField(UserProfile,
                                        on_delete=models.CASCADE,
                                        null=True)
    student_class = models.CharField(null=True)
    assignment_upload = models.ForeignKey(Assignment,
                                          on_delete=models.CASCADE,
                                          null=True,
                                          blank=True)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
