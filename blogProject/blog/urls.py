from django.urls import path
from . views import add_blog

app_name= "blog"

urlpatterns = [


path("add/",views.add_blog, name="new_blog") ,
path("Posts/",views.show_post, name="show_post")

]
