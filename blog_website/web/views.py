from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import blogPost

# Create your views here.


def home_page(request):

    return render(request, "base.html")

def read_post(request : HttpRequest):
    post_list = blogPost.objects.all()

    return render(request, "readPost.html", {"Posts": post_list})



def add_post(request: HttpRequest):

    if request.method == "POST":
        new_post = blogPost(title=request.POST["title"], content= request.POST["content"], publish_date=request.POST["publish_date"], is_published=request.POST["is_published"])
        new_post.save()
    return render(request, "addPost.html")
