from django.urls import path
from api import views

urlpatterns = [
    path('', views.Homeview.as_view()),
    path('register', views.RegisterView.as_view())
]
