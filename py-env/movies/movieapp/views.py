from django.shortcuts import render, get_object_or_404
from .models import Movie, Theater


# Create your views here.
def index (request):
    return render(request, 'movieapp/index.html')

def getmovies(request):
    movie_list=Movie.objects.all()
    return render(request, 'movieapp/movies.html', {'movie_list': movie_list})

def gettheaters(request):
    theater_list=Theater.objects.all()
    return render(request, 'movieapp/theaters.html', {'theater_list': theater_list})

def getdetails(request, id):
    mov=get_object_or_404(Movie, pk=id)
    movtheater=Theater.objects.filter(user_id=id)
    context={
        'mov': mov,
        'movtheater':movtheater,
    }
    return render(request, 'movieapp/moviedetails.html', context=context)