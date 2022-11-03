from django.urls import path
from . import views

app_name = "WebSiteblog"

urlpatterns = [
    
    path("home/", views.home, name="home"),
    
    path("add/", views.add_post, name="add_post"),
    path("list/", views.home, name = "home"),
    path("all_posts", views.all_post, name = "all_posts"),

]