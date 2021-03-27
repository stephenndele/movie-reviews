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
    reviews = Review.objects.filter(movie=id).order_by('-comment')
    
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

def edit_review(request, movie_id, review_id):
    if request.user.is_authenticated():
        movie = Movie.objects.get(id=movie_id)

        review = Review.objects.get(movie=movie, id=review_id)

        # check id user is logged in is the one who did review
        if request.user == review.user:
            # give permissions
            if request.method == 'POST':
                form = ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("main:details", movie_id)
            else:
                form = ReviewForm(instance= review)
            return render(request, "main/editreview.html", {'form': form})
        else:
            retrun redirect('main:details', movie_id)
    else:
        return redirect("accounts:login")








