from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Post
from datetime import datetime
# Create your views here.


def home(request: HttpRequest):
    posts_list = Post.objects.all()
    return render(request, "WebSiteblog/index.html", {"posts" : posts_list})
def all_post(request: HttpRequest):
    posts_list = Post.objects.all()
    return render(request, "WebSiteblog/all_posts.html", {"posts" : posts_list})

def add_post(request:HttpRequest):

    if request.method == "POST":
        new_post = Post(post_title=request.POST["post_title"],post_content=request.POST["post_content"], publish_date=datetime.today(),author_name=request.POST["author_name"] ,is_published=request.POST["is_published"])
        new_post.save()
        
     
    return render(request, "WebSiteblog/add_post.html")
