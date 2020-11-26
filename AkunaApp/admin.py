from django.contrib import admin
from .models import Produit,Client,Categorie,Commande

admin.site.register(Produit)
admin.site.register(Client)
admin.site.register(Commande)
admin.site.register(Categorie)

