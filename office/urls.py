from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_pat, name='list_patients')
]