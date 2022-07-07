from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    # titles = ', '.join([m.title for m in movies])
    return render(request=request, template_name='index.html', context={'movies': movies})
    # Since Django search step by step in paths it is better to have movies/index.html


def detail(request, movie_id):
    # try:
    #     movie = Movie.objects.get(pk=movie_id)
    #     return render(request=request, template_name='detail.html', context={'movie': movie})
    #     # we are naming template like their functions
    # except Movie.DoesNotExist:
    #     raise Http404()
    movie = get_object_or_404(klass=Movie, pk=movie_id)
    # the function get_object_or_404 implements all the try, except logic above
    return render(request=request, template_name='detail.html', context={'movie': movie})
