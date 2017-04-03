from django.shortcuts import render
from .models import Person
from .forms import PersonForm
from ldap import search_by_user


# Create your views here.
def index(request):
    form = PersonForm()
    return render(request, 'index.html', {'form' : form})

def ldap(request):
    form = PersonForm()
    return render(request, 'ldap.html', {'form': form})

def host(request):
    form = PersonForm()
    return render(request, 'host.html', {'form': form})

def ldapresult(request):
    f = PersonForm(request.POST)
    if f.is_valid():
        data = f.cleaned_data
        field = str(data['name'])
        search_by_user(field)
        out_arr = []
        out_result = open('www\\modules\\out.txt', 'r')
        for i in out_result:
            out_arr.append(i.strip('\n'))

        length = int(len(out_arr))

    return render(request, 'response.html', {'name': field,
                                             'response': out_arr,
                                             'arr_length' : length,
                                             'more' : "/ldap"
                                             })

def hostresult(request):
    f = PersonForm(request.POST)
    if f.is_valid():
        data = f.cleaned_data
        field = str(data['name'])
        search_by_user(field)
        out_arr = []
        out_result = open('www\\modules\\out.txt', 'r')
        for i in out_result:
            out_arr.append(i.strip('\n'))

        length = int(len(out_arr))

    return render(request, 'response.html', {'name': field,
                                             'response': out_arr,
                                             'arr_length' : length,
                                             'more': "/host"
                                             })


