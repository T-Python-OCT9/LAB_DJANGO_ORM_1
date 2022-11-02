from datetime import date
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Blog

# Create your views here.

def home(request:HttpRequest):
    blogs = Blog.objects.all()
    context={"blog" : blogs}
    return render(request, "app1/blog1.html" , context)

def add_blog(request:HttpRequest):


    if request.method == "POST":
        new_blog= Blog(title=request.POST["title"], description= request.POST["content"],is_published=True, publish_date=date.today(), )
        new_blog.save()

    return render(request, "app1/addblog.html")
