from django.urls import path

from . import views
from .views import ProfileCreateView

app_name = 'profiles'

urlpatterns = [
    path('', views.ProfileListView.as_view(), name='profile-list'),
    path('create/', ProfileCreateView.as_view(), name='create-profile'),
    path('<str:name>/', views.ProfileDetailView.as_view(), name='profile-detail'),
]