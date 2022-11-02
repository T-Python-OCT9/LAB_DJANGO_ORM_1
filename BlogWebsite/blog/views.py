from django.shortcuts import render
from django.http import HttpRequest ,HttpResponse
from .models import Blog

# Create your views here.

def home(request :HttpRequest):
    
    return render(request  , "blogs/home.html")


def read_blog_post(request :HttpRequest):
    view_blogs = Blog.objects.all()
    return render(request  , "blogs/read_blog.html" , {"blogs" : view_blogs})



def add_blog_post (request :HttpRequest):
     if request.method == "POST":
        new_blog = Blog(title = request.POST ["title"] , content = request.POST ["content"] ,is_published = request.POST["is_published"] ,publish_date = request.POST["publish_date"] )
        new_blog.save()
     return render(request , "blogs/add_blog.html")
