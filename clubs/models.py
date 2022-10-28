from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Club(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    play_times = models.CharField(max_length=600)
    location = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    image = models.ImageField(
        upload_to='images/', default='../polo-default_wsqwtv', blank=True
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.id} {self.name}'


def create_club(sender, instance, created, **kwargs):
    if created:
        Club.objects.create(owner=instance)


post_save.connect(create_club, sender=User)
