# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:post_pk>/', views.post_detail, name='post_detail'),
    path('posts/post_create/', views.post_create, name='post_create'),
    path('posts/<int:post_pk>/post_delete/', views.post_delete, name='post_delete'),
    path('posts/<int:post_pk>/post_update/', views.post_update, name='post_update'),
    path('posts/<int:post_pk>/comments/', views.post_comments_create, name='post_comments_create'),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/delete', views.post_comments_delete, name='post_comments_delete'),
    # path('posts/<int:post_pk>/comments/<int:comment_pk>/update', views.post_comments_update, name='post_comments_update'),
    path('posts/<int:post_pk>/post_likes/', views.post_likes, name='post_likes'),
]
