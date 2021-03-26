from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)

        if form.is_valid():
            user = form.save()

            raw_password = form.cleaned_data['password1']

            user = authenticate(username=user.username, password=raw_password)

            login(request, user)

            return redirect("main:home")

    else:
        form = RegistrationForm()

    return render(request, "accounts/register.html", {"form": form})

