from django.urls import path
from .views import HomeView,updateProduitCommande

urlpatterns = [
    path('',HomeView.as_view(),name='Akuna-Accueil'),
    path('update_commande/',updateProduitCommande,name='update-commande'),
]