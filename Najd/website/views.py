from django.shortcuts import render
from django.http import HttpRequest 
from django.http import HttpResponse
from .models import Post

# Create your views here.


def home(request: HttpRequest):
    return render(request, 'website/index.html')


def List_all_post(request:HttpRequest):
    post_list = Post.objects.all()

    return render(request, "website/list_post.html", {"post" : post_list})




def add_post(request: HttpRequest):

    if request.method == "POST":
        new_post = Post(title=request.POST["title"], Content= request.POST["Content"], is_published = request.POST["is_published"],publish_date= request.POST["publish_date"])
        new_post.save()
        

    return render(request, "website/add_post.html")

