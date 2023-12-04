from django.urls import path
from registration import views

urlpatterns = [
    path("login/", views.login_page, name='login'),
    path("signup/", views.signup, name='signup'),
    path("logout/", views.logout_page, name='logout'),
]