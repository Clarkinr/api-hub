from django.db import models
from django.contrib.auth.models import User


class Club(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    play_times = models.CharField(max_length=600, blank=True)
    location = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../polo-default_wsqwtv', blank=True
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.id} {self.name}'
