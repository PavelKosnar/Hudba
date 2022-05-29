import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from hudba.models import Band, Genre


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

    class Webscrape:
        output = []
        for genre in genres:
            link = "https://cs.wikipedia.org/wiki/" + genre.name
            response = requests.get(url=link)
            soup = BeautifulSoup(response.content, 'html.parser')
            item = soup.select('p')[0]
            para = item.text
            addition = para[:30] + "..."
            output.append(addition)

    context = {
        'genres': genres,
        'bands': bands,
        'output': Webscrape.output
    }
    return render(request, 'genres.html', context=context)
