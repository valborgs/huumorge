from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from humorge.models import FreeBoard, HumorBoard, FreeComment, HumorComment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from humorge.forms import FreePostForm, HumorPostForm

# Create your views here.

def mainpage(request):
    return render(request, 'humorge/index.html')

def freeboard(request):
    datas = FreeBoard.objects.order_by('-date').prefetch_related('free_comments')
    return render(request, 'humorge/freeboard.html', {'datas': datas})

def free_post_detail(request, pk):
    data = get_object_or_404(FreeBoard, pk=pk)
    return render(request, 'humorge/free_post.html', {'data': data})

def humorboard(request):
    datas = HumorBoard.objects.order_by('-date').prefetch_related('humor_comments')
    return render(request, 'humorge/humorboard.html', {'datas': datas})

def humor_post_detail(request, pk):
    data = get_object_or_404(HumorBoard, pk=pk)
    return render(request, 'humorge/humor_post.html', {'data': data})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            auth_login(request, user)
            return redirect("humorge:mainpage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request, 'humorge/register.html', {'form': form})


    form = UserCreationForm
    return render(request, 'humorge/register.html', {'form': form})

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
    return render(request, 'humorge/login.html', {'form': login_form})

def myinfo(request, pk):
    datas = get_object_or_404(User, pk=pk)
    return render(request, 'humorge/myinfo.html', {'datas': datas})

def free_post(request):
    form = FreePostForm()
    return render(request, 'humorge/post.html', {'form': form})

def humor_post(request):
    form = HumorPostForm()
    return render(request, 'humorge/post.html', {'form': form})
