from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Profile, CreativeField, PortfolioLink

# Create your views here.

class ProfileListView(ListView):
    model = Profile


class ProfileDetailView(DetailView):
    model = Profile
