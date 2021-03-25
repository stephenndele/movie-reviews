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