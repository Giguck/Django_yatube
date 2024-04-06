# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком постов
    path('group/', views.group_posts),
    # Страница с информацией о посте;
    # в качестве параметра ожидает целое положительное число или 0
    path('group/<int:pk>/', views.post),
]
