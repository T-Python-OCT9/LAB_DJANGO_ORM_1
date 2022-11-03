from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Fun_blog
from datetime import date

# Create your views here.

def fun_post(request: HttpRequest):
  
    if request.method == "POST":
        Add_blog = Fun_blog(Title=request.POST["Title"], Content= request.POST["Content"], is_published= request.POST["is_published"],  publish_date= request.POST["publish_date"])
        Add_blog.save()
    
      
    return render(request, "blog/post.html") 



def all_blogs(request:HttpRequest):
    list = Fun_blog.objects.all()

    return render(request, "blog/read.html", {"ALL_BLOGS" : list})
