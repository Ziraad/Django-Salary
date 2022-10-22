from django.urls import path
from . import views

app_name = 'companies'

urlpatterns = [
    path('', views.company, name='company'),
    path('add_company/', views.add_company, name='add_company'),
    path('company_detail/<str:slug>/', views.company_detail, name='company_detail'),

]
