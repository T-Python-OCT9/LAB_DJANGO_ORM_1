from django.urls import path
from .views import homePage, showPosts, addPost

app_name = 'posts'

urlpatterns = [
    path('', homePage, name='home'),
    path('read/', showPosts, name='read'),
    path('add/', addPost, name='add')
]