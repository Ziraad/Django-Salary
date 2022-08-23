from django import views
from django.urls import path
from . import views


app_name = 'salary'

urlpatterns = [
    path('', views.home, name='home_page'),
    path('salary/', views.salary, name='salary'),
]
