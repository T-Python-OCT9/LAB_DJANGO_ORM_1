from django.urls import path
from.import views


app_name="blogApp"


urlpatterns = [
    path('home/',views.blog,name="blog"),
    path('add',views.blogAdd,name="Add"),
    path('read',views.blogRead,name="Read")

]