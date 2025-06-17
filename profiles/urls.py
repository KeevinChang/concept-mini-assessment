from django.urls import path

from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.ProfileListView.as_view(), name='profile-list'),
    path('create/', views.ProfileCreateView.as_view(), name='create-profile'),
    path('<str:name>/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('<str:name>/delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
]