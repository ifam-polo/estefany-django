from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="recipes-home"), #home
    path('recipes/<int:id>/', views.recipe, name="recipes-recipe"), #details
]