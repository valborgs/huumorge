from django.urls import path, re_path
from .views import mainpage, freeboard, humorboard, free_post_detail, humor_post_detail, register, login, logout, myinfo, free_post, humor_post

app_name = 'humorge'

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('freeboard/', freeboard, name='freeboard'),
    path('freeboard/<int:pk>/', free_post_detail, name='freepostdetail'),
    path('humorboard/', humorboard, name='humorboard'),
    path('humorboard/<int:pk>/', humor_post_detail, name='humorpostdetail'),
    path('register/', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('accounts/login/', login, name='login'),
    path('myinfo/<int:pk>/', myinfo, name='myinfo'),
    path('post_humor/', humor_post, name='humor_post'),
    path('post_free/', free_post, name='free_post')
]
