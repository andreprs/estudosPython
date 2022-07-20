from django.shortcuts import render


def outro_metodo(request):
    return render(request, 'sobre/bla.html')
