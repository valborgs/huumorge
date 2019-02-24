from django.urls import path, re_path
from .views import mainpage, freeboard, humorboard, free_post_detail, humor_post_detail, free_post, humor_post, free_post_remove, humor_post_remove, free_post_mod, humor_post_mod, free_post_comment, humor_post_comment

app_name = 'humorge'

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('freeboard', freeboard, name='freeboard'),
    path('freeboard/<int:pk>', free_post_detail, name='freepostdetail'),
    path('post_free', free_post, name='free_post'),
    path('freeboard/<int:pk>/remove', free_post_remove, name='free_post_remove'),
    path('freeboard/<int:pk>/mod', free_post_mod, name='free_post_mod'),
    path('humorboard', humorboard, name='humorboard'),
    path('humorboard/<int:pk>', humor_post_detail, name='humorpostdetail'),
    path('post_humor', humor_post, name='humor_post'),
    path('humorboard/<int:pk>/remove', humor_post_remove, name='humor_post_remove'),
    path('humorboard/<int:pk>/mod', humor_post_mod, name='humor_post_mod'),

]
