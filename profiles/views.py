from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Profile, CreativeField, PortfolioLink

# Create your views here.

class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileListView, self).get_context_data(**kwargs)
        context['role'] = self.request.session['role']
        return context


class ProfileDetailView(DetailView):
    model = Profile
