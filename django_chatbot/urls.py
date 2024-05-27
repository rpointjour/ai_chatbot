from django.urls import path
from . import views

urlpatterns = [
    path('', views.django_chatbot, name='django_chatbot'),     # specify home page ('') for the app
    path('signin', views.signin, name='signin'),
    path('register', views.register, name='register'),
    path('signout', views.signout, name='signout'),
    path('users', views.users, name='users' ),
]