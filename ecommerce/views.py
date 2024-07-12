from django.http.response import HttpResponse

def home(requests):
    return HttpResponse("Home Page")
