from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Post
from datetime import date
# HttpResponse
# Create your views here.


def home(request: HttpRequest):
    blogs_all = Post.objects.all()
    return render(request, "Blog_app/home.html", {"blogs": blogs_all})


def add_blog(request: HttpRequest):
    if request.method == "POST":
        blogs = Post(
            Title=request.POST["Title"],
            Content=request.POST["Content"],
            is_published=True if "is_published" in request.POST else False,
            publish_date=date.today())
        blogs.save()

    return render(request, "Blog_app/add_blog.html")
