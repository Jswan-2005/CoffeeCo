'''Defines URL patterns for Coffee_Co'''
from django.urls import path
from . import views

app_name = 'Coffee_Co'
urlpatterns = [
    #Home Page
    path('', views.index, name = 'index'),
    #Page that shows all Coffee Types
    path('coffeeType/', views.coffeeTypes, name='coffeeTypes'),
    #Page for a singular Coffee Type
    path('coffeeType/<int:coffeeType_id>/', views.coffeeType, name='coffeeType'),
    #Page for adding a new Coffee Type
    path('newCoffeeType', views.newCoffeeType, name = 'newCoffeeType'),
    #Page for adding a new Coffee Recipe
    path('new_recipe/<int:coffeeType_id>/', views.newCoffeeRecipe, name = 'newCoffeeRecipe'),
    #Page for editing a Coffee Recipe
    path('edit_recipe/<int:recipe_id>/', views.editCoffeeRecipe, name='editCoffeeRecipe'),
    #General Information Page
    path('coffee-info/', views.coffee_info, name='coffeeInfo'),
]