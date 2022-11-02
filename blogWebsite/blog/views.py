from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpRequest, HttpResponse

from .models import Post
# Create your views here.

def add_post(request:HttpRequest):

    if request.method == "POST":
        print(request.POST)
        new_blog = Post(title=request.POST.get('title'), content= request.POST.get('content'),is_published = request.POST.get('is_published') ,publish_date= request.POST.get('publish_date'))
        new_blog.save()
        
    return render(request, "blog/index.html")


def viwe_post(request:HttpRequest):
    blogs = Post.objects.all()
    context = {'blogs': blogs}
    return render(request, "blog/view_post.html", context)
