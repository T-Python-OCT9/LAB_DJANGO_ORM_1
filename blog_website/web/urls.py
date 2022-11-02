from django.urls import path
from . import views


app_name = "web"


urlpatterns = [

    path("", views.home_page, name="home_page"),

    path("add/", views.add_post, name="add_post"),

    path("read/", views.read_post, name="read_post")


]