from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html', context={
        'name':'Estefany Melo'
    })


def contato(request):
    return render(request,'contato.html')


def sobre(request):
    return HttpResponse("SOBRE")