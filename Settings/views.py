import pycountry
from django.shortcuts import render

def settings_view(request):
    currencies = list(pycountry.currencies) 
    return render(request, 'settings.html', {
        'currencies': currencies,
        'user': request.user,
    })
