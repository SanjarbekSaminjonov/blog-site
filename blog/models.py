from django.contrib import auth
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from .const import Const

# Create your models here.


class Post(models.Model):

    regions = Const.regions

    categories = Const.categories

    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    category = models.CharField(
        max_length=35,
        choices=categories,
        default='4',
    )
    region = models.CharField(
        max_length=35,
        choices=regions,
        default='14'
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.pk)])

    def get_region(self):
        return dict(Post.regions)[self.region]

    def get_category(self):
        return dict(Post.categories)[self.category]
