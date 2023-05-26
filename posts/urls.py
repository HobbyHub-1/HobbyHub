# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    # post
    path('', views.index, name='index'),
    path('posts/<int:post_pk>/', views.post_detail, name='post_detail'),
    path('posts/post_create/', views.post_create, name='post_create'),
    path('posts/<int:post_pk>/post_delete/', views.post_delete, name='post_delete'),
    path('posts/<int:post_pk>/post_update/', views.post_update, name='post_update'),
    path('posts/<int:post_pk>/comments/', views.post_comments_create, name='post_comments_create'),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/delete', views.post_comments_delete, name='post_comments_delete'),
    # path('posts/<int:post_pk>/comments/<int:comment_pk>/update', views.post_comments_update, name='post_comments_update'),
    path('posts/<int:post_pk>/post_likes/', views.post_likes, name='post_likes'),

    # group
    path('posts/group/', views.group_list, name='group_list'),
    path('posts/group/<int:group_pk>/', views.group_detail, name='group_detail'),
    path('posts/group/create/', views.group_create, name='group_create'),
    path('posts/group/<int:group_pk>/update/', views.group_update, name='group_update'),
    path('posts/group/<int:group_pk>/delete/', views.group_delete, name='group_delete'),
    path('posts/group/<int:group_pk>/comments/', views.group_comments_create, name='group_comments_create'),
    path('posts/group/<int:group_pk>/comments/<int:comment_pk>/delete', views.group_comments_delete, name='group_comments_delete'),
    # path('posts/group/<int:group_pk>/comments/<int:comment_pk>/update/', views.group_comments_update, name='group_comments_update'),
    path('posts/group/<int:group_pk>/group_likes/', views.group_likes, name='group_likes'),

    # 기타
    path('posts/search/', views.search, name='search'),
    path('posts/category/<str:subject>/', views.category, name='category'),
    path('posts/guide/', views.guide, name='guide'),
]   
