from django import forms 
from .models import Recipe, Requirement, Purchase, Ingredient


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

class IngredientAddForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'
        
class RequirementCreateForm(forms.ModelForm):
    class Meta:
        model = Requirement
        fields = '__all__'
        
class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'