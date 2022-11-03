from django.urls import path
from . import views

app_name = "Blogs"

urlpatterns = [
    
    path("post/", views.fun_post, name="post"),
    
    path("AllBlogs/", views.all_blogs, name="AllBlogs"),
    
    
]