from django.urls import path, include
from . import views

app_name = 'newApp'

urlpatterns = [
    path("", views.exampleView, name='example'),
    path("variable", views.variableView, name='variable')
]
