from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    intro = models.TextField()
    body = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =('-created_at',)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)