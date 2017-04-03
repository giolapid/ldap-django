from django.shortcuts import render
from .models import Person
from .forms import PersonForm
from ldap import search_by_user
import os

# Create your views here.
def index(request):
    form = PersonForm()
    return render(request, 'index.html', {'form' : form})

def result(request):
    f = PersonForm(request.POST)
    if f.is_valid():
        data = f.cleaned_data
        field = str(data['name'])
        search_by_user(field)

    return render(request, 'response.html', {'response': field})

