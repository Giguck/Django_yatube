from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.TextField(max_length=250)
    slug = models.SlugField(max_length=24)
    description = models.TextField(max_length=1024)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_groups'
    )

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(Group,
                              on_delete=models.SET_NULL,
                              related_name='group_posts',
                              null=True,
                              blank=True)
