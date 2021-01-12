from django.urls import path
from .views import HomeView,CartDetailView,AnnonymousPanierJsonView,ProduitDetailView

urlpatterns = [
    path('',HomeView.as_view(),name='Akuna-Accueil'),
    path('update_commande/',AnnonymousPanierJsonView.as_view(),name='detail_commande'),
    path('create_cart/',AnnonymousPanierJsonView.as_view(),name='create_cart'),
    path('panier/',CartDetailView.as_view(),name='cart'),
    path('add-Cart-Item/',AnnonymousPanierJsonView.as_view(),name='add_cart_item'),
    path('update_cart/',AnnonymousPanierJsonView.as_view(),name='update_cart'),
    path('<int:pk>/<slug:slug>/',ProduitDetailView.as_view(),name='detail-produit'),
]