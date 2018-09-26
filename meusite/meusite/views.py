from django.shortcuts import render

def Ola_mundo(request):
    return render(request, 'ola_mundo.html', {})

