from django.urls import path
from hudba import views

urlpatterns = [
    path('', views.index, name='index')
]
