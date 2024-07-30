from django.urls import path
from api import views

urlpatterns = [
    path('', views.Homeview.as_view()),
    path('users/', views.UserView.as_view()),
    path('register', views.RegisterView.as_view()),
    path('login', views.LoginView.as_view())
    
]
