from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("posts/", views.posts, name = "posts"),
    path("preview/",views.preview, name = "preview"),

]
