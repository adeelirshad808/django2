from django import forms
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from project.forms import UserRegisterationForm
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    print(request)
    return render(request, 'project/index.html')


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
