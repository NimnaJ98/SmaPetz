from django import views
from django.urls import path
from .views import home_view, post_view

app_name ='posts'

urlpatterns = [
    path('', home_view, name='home-view'),
    

    #endpoints
    path('posts-jason/', post_view, name='posts-view-jason'),
]
