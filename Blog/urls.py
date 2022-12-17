from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name="blogs"),
    path('post/', views.post, name="blog_post"),
]
