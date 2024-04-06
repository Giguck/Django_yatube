# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Страница со списком постов
    path('groups/', views.groups, name='group'),
    # Страница с информацией о посте;
    # в качестве параметра ожидает целое положительное число или 0
    path('group/<slug:slug>/', views.group, name='group'),
    # страница поста
    path('post/<int:post_id>/', views.post, name='post'),
]
