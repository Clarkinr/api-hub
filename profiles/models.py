from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=60, blank=False)
    wheel_size = models.TextField(blank=True)
    frame_type = models.TextField(blank=True)
    brake_type = models.TextField(blank=True)
    mallet_length = models.TextField(blank=True)
    play_style = models.TextField(blank=True)
    usual_location = models.TextField(blank=True)
    team = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_nian5i.jpg'
    )

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
