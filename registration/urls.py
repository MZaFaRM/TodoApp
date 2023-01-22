from django.contrib import admin
from django.urls import path, include
from registration import views
from homepage import views as home

urlpatterns = [
    path("login/", views.loginPage, name='login'),
    path("signup/", views.signup, name='signup'),
    path("logout/", views.logoutPage, name='logout'),
]
