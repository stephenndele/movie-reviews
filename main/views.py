from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    allMovies = Movie.objects.all()
    # print(allMovies)
    return render( request,'main/index.html')

