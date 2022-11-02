from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [   
    path("", views.add_post, name="add_post"),
    path("view/", views.viwe_post, name="view_post"),
 
]