from django import forms
from .models import *


class PublicForm(forms.ModelForm):
    conteudo = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Publicacao
        fields = ('conteudo',)


class CommentForm(forms.ModelForm):
    conteudo = forms.CharField(widget=forms.Textarea, max_length=200)

    class Meta:
        model = Comentario
        fields = ('conteudo',)
