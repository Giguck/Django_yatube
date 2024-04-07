from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post, Group


# posts/views.py
# Главная страница
def index(request):
    groups = Group.objects.all()
    # В словаре context отправляем информацию в шаблон
    context = {
        'groups': groups,
    }
    return render(request, 'posts/index.html', context)


def posts(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/posts.html', context)


def group(request, slug):
    posts = Post.objects.filter(group=Group.objects.get(slug=slug))
    context = {
        'posts': posts
    }
    return render(request, 'posts/group.html', context)


def post(request, post_id):
    context = {
        'title': "Тут можно посмотреть полный текст поста",
        'post_id': post_id
    }
    return render(request, 'posts/post.html', context)
