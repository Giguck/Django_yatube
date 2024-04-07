# posts/urls.py
from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Страница со списком постов
    path('posts/', views.posts, name='posts'),
    # Страница с информацией о посте;
    # в качестве параметра ожидает целое положительное число или 0
    path('group/<slug:slug>/', views.group, name='group'),
    # страница поста
    path('post/<int:post_id>/', views.post, name='post'),
]
