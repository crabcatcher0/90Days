from django.urls import path
from accounts import views

urlpatterns = [
    path('register', views.RegisterView.as_view()),
    path('login', views.LoginView.as_view()),
    path('user/', views.UserView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('feed', views.PostView.as_view()),
    path('feed/<int:pk>/', views.PostView.as_view()),
    path('feed/delete/<int:pk>', views.PostView.as_view()),
    path('feed/edit/<int:pk>', views.PostView.as_view()),

]
