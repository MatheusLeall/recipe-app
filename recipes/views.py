from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "recipes/home.html")


def contact(request: HttpRequest) -> HttpResponse:
    return render(request, "recipes/contact.html")


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "recipes/about.html")
