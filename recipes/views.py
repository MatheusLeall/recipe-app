from django.http import HttpRequest
from django.http import HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Home view")


def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Contact view")


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse("About view")
