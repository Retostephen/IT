from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import RegistrationForm


def home(request):
    return render(request, "pages/home.html")


def about(request):
    return render(request, "pages/about.html")


def contact(request):
    return render(request, "pages/contact.html")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect("register")
    else:
        form = RegistrationForm()
    return render(request, "pages/register.html", {"form": form})
