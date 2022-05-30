from django.shortcuts import render
from django.views.generic import DetailView, ListView
from hudba.models import Band, Genre
from hudba.data_manager import bandscsv, bandssql, genrescsv, genressql


def index(request):
    num_bands = Band.objects.all().count()
    bands = Band.objects.order_by('-title')[:3]
    context = {
        'num_bands': num_bands,
        'bands': bands
    }
    return render(request, 'index.html', context=context)


def bandlist(request):
    class BandListView(ListView):
        model = Band
        context_object_name = 'bands'
    bands = Band.objects.order_by('title')

    bandscsv()
    bandssql()

    context = {
        'bands': bands
    }
    return render(request, 'band-list.html', context=context)


class BandDetailView(DetailView):
    model = Band
    template_name = 'band.html'
    context_object_name = 'band'


def genres(request):
    genres = Genre.objects.order_by('name')
    bands = Band.objects.order_by('title')

    genrescsv()
    genressql()

    context = {
        'genres': genres,
        'bands': bands
    }
    return render(request, 'genres.html', context=context)

