from django.urls import path
from . import views

urlpatterns = [
    path("", views.simpleView)
]

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('test/', views.test, name='test'),
#     path('<int:num_page>/', views.numPage_view),
#     path('<str:topic>/', views.new_view, name='topic-page'),
#
# ]
