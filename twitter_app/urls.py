from django.urls import path, include
from twitter_app.views import *

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('home/', home, name='home'),
    path('publicar/', publicar, name='novapub'),
    path('perfil/<str:user>', perfil, name='perfil'),
    path('perfil/seguir/<str:user>', seguir, name='seguir'),
    path('comentario/<int:pub_id>', comentario, name='comentario'),
    path('detalhes/<int:pub_id>', detalhes_pub, name='detalhes'),
]
