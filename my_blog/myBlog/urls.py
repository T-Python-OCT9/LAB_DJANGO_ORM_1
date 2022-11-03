from django.urls import path 
from . import views

app_name = "my_blog"

urlpatterns = [
path("base/", views.base, name="home"),
path("post/", views.add_posts, name="add_post"),
path("read/", views.read, name="read_post")
]
