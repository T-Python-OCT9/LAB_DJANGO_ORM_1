from django.shortcuts import render, resolve_url, redirect
from django.http import HttpRequest, HttpResponse
from .models import add_post


# Create your views here.


def base(request : HttpRequest):
  return render(request, 'base.html')

def add_posts(request : HttpRequest):
  if request.method == "POST":
    new_post = add_post(Title=request.POST["Title"], Content = request.POST["Content"], publish_date = request.POST['publish_date'], is_published = request.POST['is_published'])
    new_post.save()

  return render (request, 'post.html')

def read(request : HttpRequest):
  all_posts = add_post.objects.all()
  return render (request , 'read.html', {'Posts' : all_posts})

