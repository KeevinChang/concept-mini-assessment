from django.urls import path

from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.ProfileListView.as_view(), name='profile-list'),
    path('<str:name>/', views.ProfileDetailView.as_view(), name='profile-detail'),
]