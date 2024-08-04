from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_book/', views.BookCreate.as_view(),name='create_book'),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book_details'),
    path('my_view', views.my_view, name='my_view')
]
