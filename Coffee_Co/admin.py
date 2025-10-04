from django.contrib import admin
from .models import CoffeeType, CoffeeRecipeEntry

# Register your models here.
admin.site.register(CoffeeType)
admin.site.register(CoffeeRecipeEntry)