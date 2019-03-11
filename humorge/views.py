# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from humorge.models import FreeBoard, HumorBoard, FreeComment, HumorComment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import UpdateView
from django.db.models import Q
from humorge.forms import FreePostForm, HumorPostForm, FreeCommentForm, HumorCommentForm


# Create your views here.

def mainpage(request):
    return render(request, 'humorge/index.html')

def freeboard(request):
    data = FreeBoard.objects.order_by('-date').prefetch_related('free_comments')
    paginator = Paginator(data, 12)
    page = request.GET.get('page')
    datas = paginator.get_page(page)
    return render(request, 'humorge/freeboard.html', {'datas': datas})

def free_post_detail(request, pk):
    data = get_object_or_404(FreeBoard, pk=pk)
    if request.method == "POST":
        comment_form = FreeCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.freeboard = data
            comment.author = request.user
            comment.date = timezone.now()
            comment.save()
            return redirect("humorge:freepostdetail", pk=data.pk)
    else:
        comment_form = FreeCommentForm()
    return render(request, 'humorge/free_post.html', {'data': data, 'form': comment_form})

def free_post_remove(request, pk):
    data = get_object_or_404(FreeBoard, pk=pk)
    data.delete()
    return redirect("humorge:freeboard")

def humorboard(request):
    data = HumorBoard.objects.order_by('-date').prefetch_related('humor_comments')
    paginator = Paginator(data, 12)
    page = request.GET.get('page')
    datas = paginator.get_page(page)
    return render(request, 'humorge/humorboard.html', {'datas': datas})

def humor_post_detail(request, pk):
    data = get_object_or_404(HumorBoard, pk=pk)
    if request.method == "POST":
        comment_form = HumorCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.humorboard = data
            comment.author = request.user
            comment.date = timezone.now()
            comment.save()
            return redirect("humorge:humorpostdetail", pk=data.pk)
    else:
        comment_form = HumorCommentForm()
    return render(request, 'humorge/humor_post.html', {'data': data, 'form': comment_form})

def humor_post_remove(request, pk):
    data = get_object_or_404(HumorBoard, pk=pk)
    data.delete()
    return redirect("humorge:humorboard")

@login_required
def free_post(request):
    if request.method == "POST":
        free_form = FreePostForm(request.POST)
        if free_form.is_valid():
            free_post = free_form.save(commit=False)
            free_post.author = request.user
            free_post.date = timezone.now()
            free_post.save()
            return redirect("humorge:freepostdetail", pk=free_post.pk)

    else:
        free_form = FreePostForm()
    return render(request, 'humorge/post_free.html', {'free_form': free_form})

@login_required
def humor_post(request):
    if request.method == "POST":
        form = HumorPostForm(request.POST)
        if form.is_valid():
            humor_post = form.save(commit=False)
            humor_post.author = request.user
            humor_post.date = timezone.now()
            humor_post.save()
            return redirect("humorge:humorpostdetail", pk=humor_post.pk)

    else:
        form = HumorPostForm()
    return render(request, 'humorge/post_humor.html', {'form': form})


@login_required
def free_post_mod(request, pk):
    data = get_object_or_404(FreeBoard, pk=pk)
    if request.method == "POST":
        free_form = FreePostForm(request.POST, instance=data)
        if free_form.is_valid():
            free_post = free_form.save(commit=False)
            free_post.author = request.user
            free_post.save()
            return redirect("humorge:freepostdetail", pk=free_post.pk)

    else:
        free_form = FreePostForm(instance=data)
    return render(request, 'humorge/post_free.html', {'free_form': free_form})

@login_required
def humor_post_mod(request, pk):
    data = get_object_or_404(HumorBoard, pk=pk)
    if request.method == "POST":
        humor_form = HumorPostForm(request.POST, instance=data)
        if humor_form.is_valid():
            humor_post = humor_form.save(commit=False)
            humor_post.author = request.user
            humor_post.save()
            return redirect("humorge:humorpostdetail", pk=humor_post.pk)

    else:
        humor_form = HumorPostForm(instance=data)
    return render(request, 'humorge/post_humor.html', {'form': humor_form})

@login_required
def free_post_comment(request, pk):
    post = get_object_or_404(FreeBoard, pk=pk)
    if request.method == "POST":
        comment_form = FreeCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.freeboard = free_post
            comment.save()
            return redirect("humorge:freepostdetail", pk=free_post.pk)
    else:
        comment_form = FreeCommentForm()
    return render(request, 'humorge/free_comment.html', {'form': comment_form})

@login_required
def humor_post_comment(request, pk):
    post = get_object_or_404(HumorBoard, pk=pk)
    if request.method == "POST":
        comment_form = HumorCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.humorboard = humor_post
            comment.save()
            return redirect("humorge:humorpostdetail", pk=humor_post.pk)
    else:
        comment_form = HumorCommentForm()
    return render(request, 'humorge/humor_comment.html', {'form': comment_form})


def post_search(request):
    query = request.GET.get('q')
    results = FreeBoard.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    paginator = Paginator(results, 12)
    page = request.GET.get('page')
    datas = paginator.get_page(page)
    return render(request, 'humorge/freeboard.html', {'datas':datas})
