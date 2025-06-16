from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('set-role/<str:role>/', views.set_role, name='set_role'),
]