from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *


def home(request):
    return render(request, 'twitter_app/home.html')


def publicar(request):
    if request.method == 'POST':
        form = PublicForm(request.POST)
        if form.is_valid():
            form = form.save()
            form.refresh_from_db()
            form.usuario = Pessoa.objects.get(usuario=request.user)
            form.save()
    else:
        form = PublicForm()

    return render(request, 'twitter_app/publicacao.html', {'form': form})

