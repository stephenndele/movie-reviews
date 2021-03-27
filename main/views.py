from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    allMovies = Movie.objects.all()
    context = {
        "movies": allMovies,
    }

    return render( request,'main/index.html', context)

def details(request, id):
    movie = Movie.objects.get(id=id)
    reviews = Review.objects.filter(movie=id)
    
    context = {
        "movie": movie,
        "reviews": reviews
    }

    return render( request,'main/details.html', context)
@login_required()
def add_movies(request):
    if request.method == 'POST':
        form = MovieForm(request.POST or None)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:home")
    else:
        form = MovieForm()
    return render(request, 'main/addmovies.html', {'form': form, "controller":"Add Movies"}) 

@login_required()
def edit_movies(request, id):
    movie = Movie.objects.get(id=id)

    if request.method == 'POST':
        form = MovieForm(request.POST or None, instance=movie)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:details", id)
    else:
        form = MovieForm(instance=movie)
    return render(request,'main/addmovies.html', {"form": form, "controller":"Edit Movies"})

@login_required()
def delete_movies(request, id):

    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect("main:home")


def add_review(request, id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=id)
        if request.method == 'POST':
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST['comment']
                data.rating = request.POST['rating']
                data.user = request.user
                data.movie = movie
                data.save()
                return redirect("main:details", id)
        else:
            form = ReviewForm()
        return render(request, "main/details.html", {'form': form})
    else:
        return redirect("accounts:login")





