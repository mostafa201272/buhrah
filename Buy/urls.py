from django.urls import path
from . import views

urlpatterns = [
    path('', views.buy_search_page, name="buy_search_page")
]
