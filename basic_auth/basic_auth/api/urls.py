from django.urls import path
from rest_framework import views
from api import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('user/', views.UserView.as_view(), name='user-list'),
    path('user/<int:id>/', views.UserView.as_view(), name='user-detail'),
]
