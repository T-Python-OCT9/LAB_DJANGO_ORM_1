from django.urls import path
from . views import add_blog

app_name= "blog"

urlpatterns = [


path("add/", add_blog , name="new_blog") ,

]
