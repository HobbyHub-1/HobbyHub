# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:post_pk>/', views.post_detail, name='post_detail'),
    path('posts/post_create/', views.post_create, name='post_create'),
    path('posts/<int:post_pk>/post_update/', views.post_update, name='post_update'),
    path('posts/<int:post_pk>/post_delete/', views.post_delete, name='post_delete'),
]
