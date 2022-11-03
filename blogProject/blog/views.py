from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import random
from .models import Blog 
# Create your views here.


def add_blog (request: HttpRequest):

    if request.method == "POST":
        
        newBlog= Blog(Title=request.POST["Title"] , Content=request.POST["Content"], is_published="true" , publish_date= request.POST["publish_date"])
        newBlog.save()
    return render(request,"blog/Add_blog.html")


def all_post (request:HttpRequest):
    allPosts = Blog.objects.all()

    return render(request , "blog/show_post.html", {"Post": allPosts})