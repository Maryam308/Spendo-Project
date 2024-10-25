from django.shortcuts import render

def goals_view(request):
    return render(request, 'goals.html')
