from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models.base import Model

# You might want to remove this and attach your other models directly to the default User model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Registered account'
        verbose_name_plural = 'Registered accounts'

    def __str__(self):
        return self.user.username

# Model for teacher must hold data only related specifically to the Teacher
class Teacher(models.Model):
    teacher_name = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return self.teacher_name

class Student(models.Model):
    student_name = models.OneToOneField(UserProfile,
                                        on_delete=models.CASCADE,
                                        null=True)
    student_class = models.CharField(null=True)


    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


# This holds all the grading and stuff for a submission of an assignment
class Submissions(models.Model):
    submitted_by = models.OneToOneField(Student, null=False)
    submission_file = models.FileField(null=False)
    marks_obtained = models.FloatField(default=0.0)
    

class Assignment(models.Model):
    assignment_creator = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    upload_assignment = models.FileField(null=True)
    task_details = models.FileField(null=True)
    
    class Meta:
        verbose_name = 'Assignment'
        verbose_name_plural = 'Assignments'


