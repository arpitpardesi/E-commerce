from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
from .forms import ReviewForm


# Create your views here.
def list(request):
    allCars = models.Car.objects.all()
    context = {'all_cars': allCars}
    return render(request, 'cars/list.html', context=context)


def add(request):
    print(request.POST)
    if request.POST:
        brand = request.POST['brand']
        year = request.POST['year']
        models.Car.objects.create(brand=brand, year=year)

        return redirect(reverse('cars:list'))

    else:
        return render(request, 'cars/add.html')


def delete(request):
    if request.POST:
        pk = request.POST['pk']

        try:
            models.Car.objects.get(pk=pk).delete()
            return redirect(reverse('cars:list'))
        except:
            print("pk not found")
            return redirect(reverse('cars:delete'))

    return render(request, 'cars/delete.html')


def rental_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect(reverse('cars:thank_you'))

    else:
        form = ReviewForm()
    return render(request, 'cars/rental_review.html', context={'form':form})


def thank_you(request):
    return render(request, 'cars/thank_you.html')
