from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def core(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render())
    # return HttpResponse("Hello world!")