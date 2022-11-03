from multiprocessing import context
from turtle import title
from webbrowser import get
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


from .models import Post
# Create your views here.

def Blog_page (request: HttpRequest):
    
    if request.method == "POST":
        print(request.POST)
        add_blog = Post (title=request.POST.get('title'),content = request.POST.get('content'),is_published=request.POST.get('is_published'),publish_date= request.POST.get('publish_date'))
        add_blog.save()
    return render(request ,"Blogs/base.html")


def show_post (request:HttpRequest):
    blogs = Post.objects.all()
    context ={'blogs': blogs}
    return render(request,'Blogs/show.html',context)    