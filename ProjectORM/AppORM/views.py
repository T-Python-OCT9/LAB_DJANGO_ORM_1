
from django.shortcuts import  render
from django.http import HttpRequest, HttpResponse
from datetime import date
from .models import Post

# ------------ HOME PAGE -----------------
def home(request: HttpRequest):
    return render(request , "AppORM/base.html")



# ------------ CREATE NEW BLOG -----------------
def add_blog(request: HttpRequest):
    if request.method == "POST":

        new_blog = Post(
            Title=request.POST["Title"],
            Content= request.POST["Content"],
            is_published= True if "is_published" in request.POST else False,
            publish_date= request.POST["publish_date"]
            )
            
        new_blog.save()
    return render(request, "AppORM/add_blog.html")

# ------------ All BLOGS PAGE -----------------
def all_blogs(request:HttpRequest):
    blogs_list = Post.objects.all()
    return render(request, "AppORM/list_blogs.html", {"blogs" : blogs_list})
