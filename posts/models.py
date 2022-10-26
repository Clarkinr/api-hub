from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=500)
    image = models.ImageField(
        upload_to='images/', default='../polo-default_wsqwtv', blank=True
    )

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return f'{self.id} {self.title}'
