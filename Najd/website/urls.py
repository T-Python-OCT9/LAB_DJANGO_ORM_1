from django.urls import path
from . import views


app_name = "website"

urlpatterns = [

    path("", views.home, name="home"),
    path("add/", views.add_post, name="add_post"),
    path("list/", views.List_all_post, name = "list_all_post"),

]