from django.urls import path

from .views import login_user, register, log_out, user_panel, edit_profile

app_name = 'account'
urlpatterns = [
    path('login', login_user, name='login'),
    path('register', register, name='register'),
    path('log-out', log_out, name='log-out'),
    path('user', user_panel, name='user_panel'),
    path('user/edit', edit_profile, name='edit_profile'),
]
