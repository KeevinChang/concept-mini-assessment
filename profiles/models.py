from django.db import models

# Create your models here.

class CreativeField(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profiles/', default='profiles/default.jpg', blank=True)
    bio = models.TextField()
    creative_fields = models.ManyToManyField(CreativeField)

    def __str__(self):
        return self.name


class PortfolioLink(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='portfolio_links')
    link = models.URLField()

    def __str__(self):
        return self.link