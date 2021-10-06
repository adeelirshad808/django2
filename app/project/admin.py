from django.contrib import admin
from .models import UserProfile, Student, Assignment, Teacher
# Register your models here.,

admin.site.site_header = 'AMS'
admin.site.index_title = 'AMS Admin Panel'

admin.site.register(UserProfile)
admin.site.register(Student)
admin.site.register(Assignment)
admin.site.register(Teacher)