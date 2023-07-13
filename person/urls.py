from django.urls import path
from . import views

app_name = 'person'

urlpatterns = [
    path('persons/', views.persons, name='persons'),
    path('add_person/', views.add_person, name='add_person'),
    path('person_detail/<str:nation_code>/', views.person_detail, name='person_detail'),
    path('decrees/', views.decrees, name='decrees'),
    path('add_decree/', views.add_decree, name='add_decree'),
    # path('add_decree/<slug:personal_code>/', views.add_person_decree, name='add_person_decree'),
    path('wages/', views.wages, name='wages'),
    path('add_wage/', views.add_wage, name='add_wage'),
    path('wage_detail/<int:wage_id>/<str:wage_year>/', views.wage_detail, name='wage_detail'),
]
