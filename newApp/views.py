from django.shortcuts import render

# Create your views here.

def exampleView(request):
    return render(request, 'newApp/example.html')

def variableView(request):
    dict = {"firstName":"Arpit", "lastName": "Pardesi"}
    return render(request, 'newApp/variable.html', context=dict)