from django.urls import path, include
from twitter_app import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('home/', views.home, name='home'),
    path('publicar/', views.publicar, name='novapub'),

]
