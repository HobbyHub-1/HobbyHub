#accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='password'),
    path('<str:username>/delete/', views.delete, name='delete'),
]
