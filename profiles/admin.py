from django.contrib import admin
from .models import Profile, CreativeField, PortfolioLink

# Register your models here.
admin.site.register(Profile)
admin.site.register(CreativeField)
admin.site.register(PortfolioLink)