from django.urls import path
from app_explorer import views

urlpatterns = [
    path('', views.home, name='home')
]
