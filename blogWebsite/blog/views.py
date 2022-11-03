from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . models import Bolg

def add_blog(request: HttpRequest):

    if request.method == "POST":
        new_book = Bolg(title=request.POST["title"], Content= request.POST["Content"], is_published= request.POST["is_published"], publish_date= request.POST["publish_date"])
        new_book.save()
        

    return render(request, "blog/addblog.html")

def list_blog(request:HttpRequest):
    books_list = Bolg.objects.all()

    return render(request, "blog/raedblog.html", {"blog" : books_list})
