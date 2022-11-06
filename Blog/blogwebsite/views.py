from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.db import models
from .models import Blog


# Create your views here.


def add_new_blog(request:HttpRequest):
    return render(request, 'blogwebsite/add.html')

def Home(request:HttpRequest):
    return render(request, 'blogwebsite/base.html')


def set_style(request: HttpRequest):
    
    style = request.GET.get("style", "light")

    respone =  redirect("books:home")
    respone.set_cookie("style" , style, max_age=60*60*24*3)
    return respone

def add_post(request : HttpRequest):

    if request.method == "POST":
        new_post = Blog(title=request.POST["title"], content = request.POST["content"], publish_date=request.POST["publish_date"], is_published = request.POST["is_published"])
        new_post.save()


    return render(request, "blogwebsite/add.html")

def blogs_list(request: HttpRequest):
    posts = Blog.objects.all()
    return render(request, "blogwebsite/view_blogs.html", {"posts" : posts})

def post_detail(request : HttpRequest, post_id : int):

    try:
        post = Blog.objects.get(id=post_id)
    except:
        return HttpResponse("Sorry this page is found! err 404")

    return render(request, "blogApp/post_detail.html", {"post" : post})



