from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello from My App</h1>")


def test(request):
    return HttpResponse("<h1>Test function under My App</h1>")


articles = {
    'tech': '<h1>Tech page</h>',
    'world': '<h1>World page</h>',
    'cricket': '<h1>Cricket page</h>'
}


def new_view(request, topic):
    try:
        # r = articles[topic]
        return HttpResponse(articles[topic])
    except:
        raise Http404("404 page not found")


def numPage_view(request, num_page):
    try:
        topic_list = list(articles.keys())
        topic = topic_list[num_page]
        return HttpResponseRedirect(reverse('topic-page', args=[topic]))


    except:
        raise Http404("404 page not found")
