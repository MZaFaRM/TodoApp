from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.db import IntegrityError


# Create your views here.
def logout_page(request):
    logout(request)
    return redirect("login")


def login_page(request):
    if request.method in ["POST"]:
        username = request.POST.get("username")
        password = request.POST.get("password")

        if user := authenticate(request, username=username, password=password):
            login(request, user)
            return redirect("home")
        else:
            return render(
                request, "login.html", {"error": "Wrong username or password"}
            )

    return render(request, "login.html")


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        re_password = request.POST.get("re-password")

        if password != re_password:
            return render(request, "signup.html", {"error": "Passwords don't match"})

        try:
            User.objects.create_user(username=username, password=password)
            return redirect("login")
        except IntegrityError:
            return render(request, "signup.html", {"error": "Username already taken"})
