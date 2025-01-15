from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import RecipeCreateForm,IngredientAddForm,RequirementCreateForm,PurchaseCreateForm
from .models import Purchase,Ingredient,Recipe
# Create your views here.

def home(request):
    return render(request, 'storage_managing/home.html')

def purchases(request):
    return render(request,'storage_managing/purchases.html')

def storage(request):
    ingredients = Ingredient.objects.all()
    return render(request,'storage_managing/storage.html', {'ingredients': ingredients})

class PurchaseCreate(CreateView):
    form_class = PurchaseCreateForm
    model = Purchase
    template_name = 'storage_managing/purchase_add.html'
    success_url = reverse_lazy('purchases')
    
class IngredientCreate(CreateView):
    form_class = IngredientAddForm
    model = Ingredient
    template_name = 'storage_managing/ingredient_add.html'
    success_url = reverse_lazy('purchases')

class IngredientEdit(UpdateView):
    form_class = IngredientAddForm
    model = Ingredient
    template_name = 'storage_managing/ingredient_edit.html'
    success_url = reverse_lazy('storage')
    