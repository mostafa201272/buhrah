"""Buhrah URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Home Page
    path('', include('Home.urls')),

    # Buy Page
    path('buy/', include('Buy.urls')),

    # Sell Page
    path('sell/', include('Sell.urls')),

    # Blog Page
    path('blog/', include('Blog.urls')),

    # Financial Page
    path('financials/', include('Financial_Solutions.urls')),

    # Financial Page
    path('contact/', include('Contact.urls')),


    # Admin Control
    path('admin/', admin.site.urls),

    # Users App
    path('users/', include('Users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    
