from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name="home"),
    path('official_name/', official_name, name="official_name"),
    path('official_name/<int:id>', specific_data, name="official_name"),
    path('add_data', add_official, name="add_data"),
    path('remove_data/<int:id>', remove_official, name="remove_data"),
    path('update_data/<int:id>', update_official, name="update_data"),
]
