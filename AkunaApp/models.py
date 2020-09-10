from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User,AnonymousUser

class Categorie(models.Model):
    """
        La classe modèle pour les catégories. 
    """
    libelle = models.CharField(_("Libelle"), max_length=500) 

    class Meta:
        managed = True
        verbose_name = 'catedgorie'
        verbose_name_plural = 'catedgories'

    def __str__(self):
        return (self.libelle)


class Produit(models.Model):
    """ 
        La classe modèle produit pour les produits.
    """
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    libelle =  models.CharField(_("Libelle"),max_length=500)
    image=models.ImageField(_("Illustration"))
    description=models.TextField(_("Description"))
    slug=models.SlugField(_('slug'))
    prix_unitaire = models.FloatField(_("Prix Unitaire"))
    quantite_stock = models.IntegerField(_("Quantite en stock"))
    
    class Meta:
        managed = True
        verbose_name = 'produit'
        verbose_name_plural = 'produits'

    def __str__(self):
        return self.libelle


class Client(User):
    """
        Class modèle pour les clients.
    """

    entreprise =  models.CharField(_("Entreprise"), max_length=500)
    commune = models.CharField(_("Commune"), max_length=500)
    quartier  = models.CharField(_("Quartier"), max_length=500)

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'

    def __str__(self):
        return ("{0} {1}".format(self.username))


class Commande(models.Model):
    """
        Classse modèle pour les commandes.
    """
    date = models.DateTimeField(_('Date'))
    etat  = models.BooleanField(_("Etat"))
    info_livraison = models.TextField(_("Informations de livraison"))
    total = models.IntegerField(_("Total"))

    class Meta:
        
        verbose_name = 'commande'
        verbose_name_plural = 'commandes'


class Liste(models.Model):
    """
        La classe modèle pour la liste de produits.
    """
    produit = models.ForeignKey(Produit,on_delete=models.DO_NOTHING)
    commande = models.ForeignKey(Commande,on_delete=models.DO_NOTHING)
    quantite = models.IntegerField(_("Quantité"))

    class Meta:
        
        verbose_name = 'liste'
        verbose_name_plural = 'listes'

