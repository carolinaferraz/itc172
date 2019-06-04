from django.shortcuts import render, get_object_or_404
from .models import Movie, Theater
from .forms import TheaterForm, MovieForm
from django.contrib.auth.decorators import login_required


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
    movtheater=Theater.objects.filter(id=id)
    context={
        'mov': mov,
        'movtheater':movtheater,
    }
    return render(request, 'movieapp/moviedetails.html', context=context)

#login/logout
def loginmessage(request):
    return render(request, 'movieapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'movieapp/logoutmessage.html')

@login_required
#add theater
def addtheater(request):
     form=TheaterForm
     if request.method=='POST':
          form=TheaterForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=TheaterForm()
     else:
          form=TheaterForm()
     return render(request, 'movieapp/addtheater.html', {'form': form})

@login_required
#add movie
def addmovie(request):
     form=MovieForm
     if request.method=='POST':
          form=MovieForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MovieForm()
     else:
          form=MovieForm()
     return render(request, 'movieapp/addmovie.html', {'form': form})
