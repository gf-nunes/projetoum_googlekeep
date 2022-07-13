from dataclasses import fields
from django import forms
from login.models import Nota

class NotaForm(forms.ModelForm):

    class Meta:
        model = Nota
        fields = ('titulo', 'texto')