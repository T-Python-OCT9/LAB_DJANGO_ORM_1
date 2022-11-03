from django.shortcuts import render, resolve_url, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date
from . models import Post
# Create your views here.

def posts (request:HttpRequest):
    posts_list = Post.objects.all()
    
    return render(request, 'blog/posts.html',{"posts_list": posts_list })

def preview (request:HttpRequest):
    if request.method =="POST":
        new_post = Post(title=request.POST["title"],content=request.POST["content"],is_published=request.POST["is_published"],publish_date=request.POST["publish_date"])
        new_post.save()
    return render(request, 'blog/preview.html') 
       