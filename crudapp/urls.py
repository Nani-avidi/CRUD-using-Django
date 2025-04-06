# crudapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crud/', views.crud_op, name='crud'),
]
