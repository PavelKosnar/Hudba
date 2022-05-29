from django.urls import path
from hudba import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bands/', views.bandlist, name='band-list'),
    path('band/<slug:slug>', views.BandDetailView.as_view(), name='band-detail'),
    path('genres/', views.genres, name='genres')
]
