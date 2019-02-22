from django.urls import path, re_path
from .views import register, login, logout, myinfo

app_name = 'users'

urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('myinfo/<int:pk>', myinfo, name='myinfo'),
]
