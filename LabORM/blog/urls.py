from django.contrib import admin
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.home, name="home"),
    path("add_blog/",views.add_blog ,name = "addblog"),
    path("raedblog/",views.raed_blog , name = "raedblog"),

]