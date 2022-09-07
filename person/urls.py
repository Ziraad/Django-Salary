from django.urls import path
from . import views

app_name = 'person'

urlpatterns = [
    path('persons/', views.persons, name='persons'),
    path('add_person/', views.add_person, name='add_person'),
    path('decrees/', views.decrees, name='decrees'),
    path('add_decree/', views.add_decree, name='add_decree'),
    # path('add_decree/<slug:personal_code>/', views.add_person_decree, name='add_person_decree'),
    path('wages/', views.wages, name='wages'),
    path('add_wage/', views.add_wage, name='add_wage'),
    path('wage_detail/<int:wage_id>/', views.wage_detail, name='wage_detail'),
    path('decree_detail/<int:decree_id>/', views.decree_detail, name='decree_detail'),
]
