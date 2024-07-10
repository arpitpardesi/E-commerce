from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('<int:num_page>', views.num_view),
    path('<str:topic>/', views.new_view),

]
