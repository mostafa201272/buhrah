from django.shortcuts import render

# Create your views here.
def buy_search_page(request):
    return render(request, 'pages/frontend/Buy/buy.html')