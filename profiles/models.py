from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
# Create your models here.

class CreativeField(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=100, unique=True)
    profile_picture = models.ImageField(upload_to='profiles/', default='profiles/default.jpg', blank=True)
    bio = models.TextField()
    creative_fields = models.ManyToManyField(CreativeField)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            old = Profile.objects.get(pk=self.pk)
            default_image = self._meta.get_field('profile_picture').default
            if old.profile_picture != self.profile_picture and old.profile_picture.name != default_image:
                if os.path.isfile(old.profile_picture.path):
                    os.remove(old.profile_picture.path)
        except Profile.DoesNotExist:
            pass
        super().save(*args, **kwargs)


@receiver(post_delete, sender=Profile)
def delete_profile_picture(sender, instance, **kwargs):
    default_image = instance._meta.get_field('profile_picture').default
    if instance.profile_picture.name != default_image and instance.profile_picture:
        file_path = instance.profile_picture.path
        if os.path.isfile(file_path):
            os.remove(file_path)


class PortfolioLink(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='portfolio_links')
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.link