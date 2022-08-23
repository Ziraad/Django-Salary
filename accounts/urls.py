from django import views
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    # path('profile/edit', views.profile_edit, name='profile_edit'),
    path('register', views.register_user, name='register_user'),
    # path('orders/', views.orders, name='orders'),
    # path('password/', views.change_pass, name='change_pass'),
    path('forgotPassword/', views.forgot_password, name='forgot_password'),
    # path('resetpassword_validate/<uidb64>/<token>/', views.reset_password_validate, name='reset_password_validate'),
    # path('resetPassword/', views.reset_password, name='reset_password'),
    path('companies/', views.company, name='company'),
    path('add_company/', views.add_company, name='add_company'),
]
