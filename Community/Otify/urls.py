from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name='Home'),
    path("Login", views.Login, name='Login'),
    path("staff", views.Staff, name='Staff'),
    path("logout", views.Logout, name='logout'),
]