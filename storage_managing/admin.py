from django.contrib import admin

# Register your models here.
from .models import Recipe, Requirement, Purchase, Ingredient

admin.site.register(Recipe)
admin.site.register(Requirement)
admin.site.register(Purchase)
admin.site.register(Ingredient)
