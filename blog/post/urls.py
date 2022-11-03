from django.urls import path
from . import views



urlpatterns = [

    path('',views.post_add, name='new_post'),
    path('posts/',views.posts,name='posts')
    #path('post/id/','<post_id/>',)
]