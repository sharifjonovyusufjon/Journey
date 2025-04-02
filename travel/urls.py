from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('travel/', views.travels, name='travels'),
    path('travel/details/<int:id>', views.details, name='details'),
]