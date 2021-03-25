from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    allMovies = Movie.objects.all()
    context = {
        "movies": allMovies,
    }

    return render( request,'main/index.html', context)

def details(request, id):
    movie = Movie.objects.get(id=id)

    context = {
        "movie": movie
    }

    return render( request,'main/details.html', context)