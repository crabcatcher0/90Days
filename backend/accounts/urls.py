from django.urls import path
from accounts import views

urlpatterns = [
    path('account/', views.HomeView.as_view())
]
