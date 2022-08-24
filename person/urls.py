from django.urls import path
from . import views

app_name = 'person'

urlpatterns = [
    path('persons/', views.persons, name='persons'),
    path('add_person/', views.add_person, name='add_person'),
    path('warrants/', views.warrants, name='warrant'),
    path('add_warrant/', views.add_warrant, name='add_warrant'),
    path('wages/', views.wages, name='wages'),
    path('add_wage/', views.add_wage, name='add_wage'),
]
