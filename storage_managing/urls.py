from django.urls import path

from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("purchases/",views.purchases, name = "purchases"),
  path("purchases/create", views.PurchaseCreate.as_view(), name = 'purchasecreate'),
  path("storage/create", views.IngredientCreate.as_view(), name = 'ingredientcreate'),
  path("storage/<pk>/edit", views.IngredientEdit.as_view(), name = 'ingredientedit'),
  path("storage/",views.storage, name = "storage"),
  ]