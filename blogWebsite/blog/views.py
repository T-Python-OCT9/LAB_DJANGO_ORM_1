from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . models import Bolg

def add_blog(request: HttpRequest):

    if request.method == "POST":
        new_blog = Bolg(title=request.POST["title"], Content= request.POST["Content"], is_published= request.POST["is_published"], publish_date= request.POST["publish_date"])
        new_blog.save()
        

    return render(request, "blog/addblog.html")


def list_blog(request: HttpRequest):
    blog_list = Bolg.objects.all()
   
    return render(request, "blog/readblog.html", {"blog_list" : blog_list})