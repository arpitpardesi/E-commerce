from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello from My App</h1>")

def test(request):
    return HttpResponse("<h1>Test function under My App</h1>")