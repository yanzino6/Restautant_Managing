from django.db import models

# Create your models here.

class Ingredient (models.Model):
    name = models.CharField(max_length=200, unique=True)
    quant = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    
    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    
class Requirement(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE,related_name='recipe_requirement')
    ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE,related_name='recipe_requirement')
    quant = models.IntegerField(models.Model)

    
class Purchase(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quant = models.IntegerField(default = 0)
    datetime = models.DateTimeField(auto_now_add=True)
    
