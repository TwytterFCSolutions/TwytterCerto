from django import forms
from .models import *


class PublicForm(forms.ModelForm):
    conteudo = forms.CharField(widget = forms.Textarea())

    class Meta:
        model = Publicacao
        fields = ('conteudo',)