from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [

    path("addblog/", views.add_blog ,name = "add_blog"),
    path("read/", views.list_blog, name = "list_blog")
]