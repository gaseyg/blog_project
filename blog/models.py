from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Post(models.Model):
    author = models.ForeignKey(
        to="User",
        on_delete=models.CASCADE,
        related_name='posts'
    )
    title = models.CharField(max_length=150)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    author = models.ForeignKey(
        to="User",
        on_delete=models.CASCADE,
        related_name='comments',

    )
    post = models.ForeignKey(
        to="Post",
        on_delete=models.CASCADE,
        related_name='comments',
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Reaction(models.Model):
    class Values(models.TextChoices):
        LIKE = 'like', 'Нравится',
        DISLIKE = 'dislike', 'Не нравится',
    
    value = models.CharField(max_length=7, choices=Values.choices, null=True)
    author = models.ForeignKey(
        to="User",
        on_delete=models.CASCADE,
        related_name='reactions',

    )
    post = models.ForeignKey(
        to="Post",
        on_delete=models.CASCADE,
        related_name='reactions',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                'author',
                'post',
                name='author_post_unique',
            ),
        ]
