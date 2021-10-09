from django import forms
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from project.models import Teacher
from project.models import Student
from project.models import Submissions
from project.models import Assignment
from project.forms import UserRegisterationForm
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    ass = Submissions.objects.all()

    assignments = ''
    t = True
    if t == False:
        if request.user.is_authenticated:
            print(request.user.is_authenticated)
            assignments = Assignment.objects.all()

        return render(request, 'project/index.html',
                      {'assignments': assignments})

    else:
        return render(request, 'project/teacher.html')

    # return render(request, 'project/index.html', )


def teacher(request):
    if request.method == "POST":
        task = request.POST.get('task')
        teacher_instance = Teacher.objects.get(teacher_name=request.user)
        task = Assignment.objects.create(assignment_creator=teacher_instance,
                                         assignment_details=task)
        print(task)
        task.save()
        return HttpResponse('task created')
    else:
        all_assignments = Submissions.objects.all()
        for sub in all_assignments:
            print(sub.submission_file)

        return render(request, 'project/teacher.html',
                      {'assignments': all_assignments})


def assignment(request):
    username = request.user
    if request.method == "POST":

        uploaded_file = request.FILES['inputFile']
        student = Student.objects.get(student_name=request.user)
        std_instance = student
        document = Submissions.objects.create(submitted_by=std_instance,
                                              submission_file=uploaded_file)
        document.save()

        return HttpResponse('you file uploaded')
    return render(request, 'project/assignment.html')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserRegisterationForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            print(user)
            registered = True
    else:
        user_form = UserRegisterationForm()

    return render(request, 'project/register.html', {
        'registered': registered,
        'user_form': user_form
    })


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                print(user.is_active)
                login(request, user)
                return render(request, 'project/index.html')
            else:
                return HttpResponse('Account is deactivated')
        else:
            return HttpResponse('Please use correct username and password')
    else:
        print('running')
        return render(request, 'project/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
