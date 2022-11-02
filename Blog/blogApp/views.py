from django.shortcuts import render
from django.http import HttpRequest
from.models import Blog




def blog (request:HttpRequest):

    return render(request,'blogApp/blog.html')



def blogAdd (request:HttpRequest):
    if request.method=="POST":
        
        new_blog= Blog(title=request.POST["title"], content=request.POST["content"],is_published=request.POST["is_published"],publish_date=request.POST["publish_date"])
        new_blog.save()
    return render(request,'blogApp/blogAdd.html')






def blogRead (request:HttpRequest):
    blog_list=Blog.objects.all()

    return render(request,'blogApp/blogRead.html',{"blogs":blog_list})







# Create your views here.
