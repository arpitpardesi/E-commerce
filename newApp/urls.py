from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.exampleView),
path("variable", views.variableView)
]