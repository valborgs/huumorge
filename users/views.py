# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import NewUserForm, UserUpdateForm, ProfileUpdateForm


# Create your views here.

def register(request):
    if request.method == "POST":
        regiform = NewUserForm(request.POST)
        if regiform.is_valid():
            user = regiform.form_save()
            username = regiform.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            auth_login(request, user)
            return redirect("humorge:mainpage")
        else:
            for msg in regiform.error_messages:
                messages.error(request, f"{msg}: {regiform.error_messages[msg]}")

            return render(request, 'humorge/register.html', {'form': regiform})

    form = NewUserForm
    return render(request, 'users/register.html', {'form': form})

def logout(request):
    auth_logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect(("humorge:mainpage"))

def login(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("humorge:mainpage")
            else:
                messages.error(request, "invalid username or password.")
        else:
            messages.error(request, "invalid username or password.")


    login_form = AuthenticationForm
    return render(request, 'users/login.html', {'form': login_form})

@login_required
def myinfo(request, pk):
    if request.method == "POST":
        userinfo_update = UserUpdateForm(request.POST, instance=request.user)
        image_update = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if userinfo_update.is_valid() and image_update.is_valid():
            userinfo_update.save()
            image_update.save()
            messages.info(request, "Your information has been changed!")
            return redirect("users:myinfo", pk)
        else:
            messages.error(request, "can't change your information!")

    userinfo_update = UserUpdateForm(instance=request.user)
    image_update = ProfileUpdateForm(instance=request.user.profile)
    datas = get_object_or_404(User, pk=pk)
    return render(request, 'users/myinfo.html', {'datas': datas, 'update':userinfo_update, 'img':image_update})
