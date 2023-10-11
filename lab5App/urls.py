from django.urls import path
from . import views

urlpatterns = [
    path('', views.display , name='display'),
    path('add/', views.add, name='add')
]