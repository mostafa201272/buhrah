from django.urls import path
from . import views

urlpatterns = [
    path('', views.financial, name="financial")
]
