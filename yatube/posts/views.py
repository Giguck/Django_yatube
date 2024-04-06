from django.shortcuts import render
from django.http import HttpResponse


# posts/views.py
# Главная страница
def index(request):
    return render(request, 'posts/index.html')


def groups(request):
    return render(request, 'posts/group.html')


def group(request, slug):
    return render(request, 'posts/group.html')


def post(request, post_id):
    return render(request, 'posts/post.html')
