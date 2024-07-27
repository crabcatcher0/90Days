from django.urls import path
from api import views


urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register'),
    path('profile/', views.UserView.as_view(), name='profile'),
    path('profile/<int:pk>/', views.UserView.as_view(), name='profile-detail'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout')

]
