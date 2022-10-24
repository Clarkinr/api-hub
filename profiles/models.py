from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=60, blank=False)
    content = models.TextField(blank=False)
    Images = models.ImageField(
        upload_to='images/', default='../Blank-Avatar_gg37ls.png'
    )

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return f"{self.owner}'s profile"

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)