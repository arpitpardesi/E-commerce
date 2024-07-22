from django.shortcuts import render
from . import models
# Create your views here.
def list_pat(request):
    all_pat = models.Patient.objects.all()
    context = {'patients':all_pat}
    return render(request, "office/list.html",context=context)