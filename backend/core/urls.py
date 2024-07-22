from django.urls import path
from core import views
urlpatterns = [
    path('students/', views.StudentApi.as_view()),
    path('students/<int:pk>', views.StudentApi.as_view())

]
