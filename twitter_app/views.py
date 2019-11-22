from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView

from .forms import *


def home(request):
    if request.user.is_authenticated:
        logado = Pessoa.objects.get(usuario=request.user)
        seguindo = logado.seguindo.all()
        publicacoes = Publicacao.objects.filter(usuario__in=seguindo).order_by('data_publicacao').reverse()[:30]
    return render(request, 'twitter_app/home.html', {'seguindo': publicacoes})


def publicar(request):
    if request.method == 'POST':
        form = PublicForm(request.POST)
        if form.is_valid():
            form = form.save()
            form.refresh_from_db()
            form.usuario = Pessoa.objects.get(usuario=request.user)
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = PublicForm()

    return render(request, 'twitter_app/publicacao.html', {'form': form})


def perfil(request, user):
    profile = User.objects.get(username=user)
    pessoa = Pessoa.objects.get(usuario=profile)
    publicacoes = Publicacao.objects.all().order_by('data_publicacao').reverse().filter(usuario=pessoa)

    return render(request, 'twitter_app/perfil.html', {'publicacoes': publicacoes, 'pessoa': pessoa})


def seguir(request, user):
    logado = Pessoa.objects.get(usuario=request.user)
    profile = User.objects.get(username=user)
    seguido = Pessoa.objects.get(usuario=profile)
    logado.seguindo.add(seguido)
    return HttpResponseRedirect(reverse('home'))


def comentario(request, pub_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            pub = Publicacao.objects.get(pk=pub_id)
            form = form.save()
            form.refresh_from_db()
            form.usuario = Pessoa.objects.get(usuario=request.user)
            form.publicacao = pub
            form.save()
            return HttpResponseRedirect(reverse('detalhes',  kwargs={'pub_id': pub_id}))
    else:
        form = CommentForm()
    return render(request, 'twitter_app/comentario.html', {'form': form})


def detalhes_pub(request, pub_id):
    try:
        comentarios = Comentario.objects.all()
        publicacoes = Publicacao.objects.all().order_by('data_publicacao').reverse().filter(pk=pub_id)


    except Publicacao.DoesNotExist:
        raise Http404('Publicação não encontrada')
    return render(request, 'twitter_app/detalhes.html',
                  {'publicacoes': publicacoes, 'comentarios': comentarios, 'pub_id': pub_id})
