from django.shortcuts import render

# Create your views here.
def financial(request):
    return render(request, 'pages/frontend/Financial_Solutions/financial_solutions.html')