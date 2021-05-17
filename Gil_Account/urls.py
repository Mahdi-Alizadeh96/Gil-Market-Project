from django.urls import path

from .views import login_user, register, log_out, user_panel, edit_profile

urlpatterns = [
    path('login', login_user),
    path('register', register),
    path('log-out', log_out),
    path('user', user_panel),
    path('user/edit', edit_profile),
]
