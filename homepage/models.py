from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User


class Priority(models.Model):
    name = models.CharField(max_length=50, unique=True)
    value = models.IntegerField(unique=True)


class TaskTypes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    points = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    deadline = models.DateTimeField()
    status = models.BooleanField(default=1)
    types = models.OneToOneField(TaskTypes, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
