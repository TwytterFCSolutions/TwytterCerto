from django.contrib import admin
from django.urls import path, include
from twitter_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('twitter_app.urls')),
]
