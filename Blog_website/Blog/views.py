from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Blog_Data

# Create your views here.

def read_blog(request:HttpRequest):
    msg_list = Blog_Data.objects.all()
    return render(request, "Blog/read_blog.html", {"msg_list" : msg_list})
    

def add_blog(request: HttpRequest):

    if request.method == "POST":
        new_msg = Blog_Data(Title=request.POST["Title"], Content= request.POST["Content"],is_published =request.POST["is_published"] ,publish_date= request.POST["publish_date"])
        new_msg.save()
        

    return render(request, "Blog/add_blog.html")
