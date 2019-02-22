from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.


@login_required
def myinfo(request, pk):
    datas = get_object_or_404(User, pk=pk)
    return render(request, 'humorge/myinfo.html', {'datas': datas})
