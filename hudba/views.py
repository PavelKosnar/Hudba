from django.shortcuts import render

from hudba.models import Band


def index(request):
    num_bands = Band.objects.all().count()
    bands = Band.objects.order_by('title')[:3]
    context = {
        'num_bands': num_bands,
        'bands': bands
    }
    return render(request, 'index.html', context=context)


