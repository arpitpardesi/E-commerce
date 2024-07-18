from django.http.response import HttpResponse
from django.shortcuts import render


def home(requests):
    return HttpResponse("Home Page")


def page_not_found(request, exception):
    return render(request, "error_Page.html", status=404)
