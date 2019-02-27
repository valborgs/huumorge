from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from .views import register, login, logout, myinfo

app_name = 'users'

urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('myinfo/<int:pk>', myinfo, name='myinfo'),
    path('password_reset', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html'), name='password_reset'
        ),
    path('password_reset_confirm/<slug:uidb64>/<slug:token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'), name='password_reset_confirm'
        ),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), name='password_reset_done'
        ),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'), name='password_reset_complete'
        ),
]
