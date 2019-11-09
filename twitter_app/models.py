from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):
    nome = models.CharField(max_length=120)
    data_criacao = models.DateField(auto_now_add=True)
    data_nascimento = models.DateField()
    seguindo = models.ManyToManyField('Pessoa', null=True, blank=True)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Comentario(models.Model):
    conteudo = models.CharField(max_length=200)
    data_comentario = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(Pessoa, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.conteudo


class Publicacao(models.Model):
    usuario = models.ForeignKey(Pessoa, null=True, blank=True, on_delete=models.SET_NULL)
    conteudo = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    comentario = models.ForeignKey(Comentario, null=True, blank=True, related_name='Comentario',
                                   on_delete=models.SET_NULL)
