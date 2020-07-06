from django.urls import path
from customer import views
urlpatterns = [
    path('index',views.index),
]
