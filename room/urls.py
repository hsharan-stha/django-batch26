from django.urls import path
from room import views
urlpatterns = [
    path('index',views.index),
]
