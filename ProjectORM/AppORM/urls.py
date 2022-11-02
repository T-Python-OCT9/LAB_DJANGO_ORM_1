from django.urls import path
from . import views

app_name = "AppORM"

urlpatterns = [
    path('', views.home , name="home"),
    path('add_blog', views.add_blog , name="add_blog"),
    path('all_blogs', views.all_blogs , name="all_blogs"),
]
