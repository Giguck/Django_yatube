from django.shortcuts import render
from django.http import HttpResponse


# posts/views.py
# Главная страница
def index(request):
    return HttpResponse('Главная страница')


# Страница со списком мороженого
def group_posts(request):
    return HttpResponse('Список мороженого')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def post(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')
