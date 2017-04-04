from django.forms import ModelForm
from .models import Person
from django import forms

class PersonForm(ModelForm):
    input = forms.CharField(max_length=100, label='')
    class Meta:
        model = Person
        fields = ['input']
