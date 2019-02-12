from django.urls import path
from .views import mainpage, freeboard, humorboard, register, login, logout, myinfo

app_name = 'humorge'

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('freeboard/', freeboard, name='freeboard'),
    path('humorboard/', humorboard, name='humorboard'),
    path('register/', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('myinfo/', myinfo, name='myinfo'),
]
