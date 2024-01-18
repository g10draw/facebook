from django.urls import path

from .views import login_user, register_user, logout_user

urlpatterns=[
    path('login', login_user, name='login-page'),
    path('register_user', register_user, name='register-page'),
    path('logout_user', logout_user, name='logout-page'),
]