from django.urls import path
from . import views

urlpatterns = [
    path('', views.sell_page, name="sell_page")
]
