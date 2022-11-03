from django.urls import path

from . import views

app_name ='blog_post'


urlpatterns = {
    path ('blog/',views.Blog_page,name='blogpage'),
    path ('view/',views.show_post,name="show_post"),


}