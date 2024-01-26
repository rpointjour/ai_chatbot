from django.urls import path
from . import views

urlpatterns = [
    path('', views.django_chatbot, name='django_chatbot')     # specify home page ('') for the app
]