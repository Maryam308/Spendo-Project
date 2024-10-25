from django.urls import path
from . import views

urlpatterns = [
    path('', views.goals_view, name='goals'),  
]
