from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.db import models

# Create your views here.


def add_new_blog(request:HttpRequest):
    return render(request, 'base.html')