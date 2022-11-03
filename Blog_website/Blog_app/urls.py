from django.urls import path
from django.http import HttpRequest, HttpResponse
from . import views

app_name = "Blog_app"


urlpatterns = [
    path('home', views.home, name="home"),
    path('add_blog', views.add_blog, name="add_blog"),
]
