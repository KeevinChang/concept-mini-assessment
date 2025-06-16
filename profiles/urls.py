from django.urls import path

from . import views
from .views import ProfileListView, ProfileDetailView

path('profiles/', ProfileListView.as_view(), name='profile-list')
path('profiles/<str:name>', ProfileDetailView.as_view(), name='profile-detail')