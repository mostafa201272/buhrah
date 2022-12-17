from django.shortcuts import render

# Create your views here.
def sell_page(request):
    return render(request, "pages/frontend/Sell/sell.html")
