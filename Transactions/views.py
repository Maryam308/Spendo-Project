from django.shortcuts import render

def transactions_view(request):
    return render(request, 'transactions.html')
