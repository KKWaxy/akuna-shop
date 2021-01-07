from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User,AnonymousUser


import datetime

class Categorie(models.Model):
    """
        La classe modèle pour les catégories. 
    """
    libelle = models.CharField(_("Libelle"), max_length=150) 
    description = models.TextField(_("Description"), max_length="500", null=True,blank=True)
    create_date =  models.DateTimeField(_('Date de création'),auto_now_add=True)
    modified_date = models.DateTimeField(_("Date demodification"),auto_now=True)

    class Meta:
        managed = True
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'

    def __str__(self):
        return (self.libelle)
    
    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})
    


class Produit(models.Model):
    """ 
        La classe modèle produit pour les produits.
    """
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    libelle =  models.CharField(_("Libelle"),max_length=500)
    image = models.ImageField(_("Illustration"),upload_to='akuna_produits')
    description = models.TextField(_("Description"))
    slug=models.SlugField(_('slug'))
    prix_unitaire = models.FloatField(_("Prix Unitaire"))
    quantite_stock = models.IntegerField(_("Quantite en stock"))    
    create_date = models.DateTimeField(_("Date de création"), auto_now_add=True)
    modified_date = models.DateTimeField(_('Date de modification'), auto_now=True)
    
    # delete_date = models.DateField(_("Date de suppresion"), auto_now=True)
    class Meta:
        managed = True
        verbose_name = 'produit'
        verbose_name_plural = 'produits'

    def __str__(self):
        return self.libelle
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("detail-produit", kwargs={"pk":self.id,"slug": self.slug})

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

class Profile(models.Model):
    """
        Classe modèle pour attribuer un profile client à chaque client.
    """
    
    client =  models.OneToOneField(Client,on_delete=models.CASCADE)
    avatar = models.ImageField(_("Photo de profile"),upload_to = "clients_avatar")
    create_date = models.DateTimeField(_("Date de création"), auto_now_add=True)
    modified_date = models.DateTimeField(_('Date de modification'), auto_now=True)
    

    class Meta:
        managed = True
        verbose_name = 'client_profile'
        verbose_name_plural = 'client_profiles'

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

    def __str__(self):
        return self.name
        

class PanierModel(models.Model):
    """
    Le modèle de panier
    """
    create_date = models.DateTimeField(_("Date de création"), auto_now_add=True)
    modified_date = models.DateTimeField(_('Date de modification'), auto_now=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'PanierModel'
        verbose_name_plural = 'PanierModels'
    
    def __str__(self):
        
        return (str(self.id))

class PanierElementModel(models.Model):
    """
    Le modèle du contenu du panier
    """
    panier = models.ForeignKey(PanierModel,on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit,on_delete=models.DO_NOTHING)
    quantite = models.IntegerField(_("Quantite"),default=1)
    date_ajout = models.DateTimeField(_("Date d'ajout"),auto_now_add=True)
    date_modif = models.DateTimeField(_("Date modification"),auto_now=True)

    class Meta:
        db_table = ''
        ordering = ['date_ajout']
        managed = True
        verbose_name = 'PanierElementModel'
        verbose_name_plural = 'PanierElementModels'
        
    def __str__(self):
        return(str(self.id))

    def total(self):
        """
        docstring
        """
        return(self.quantite*self.produit.prix_unitaire)

    def libelle(self):
        return(self.produit.libelle)
    
    def prix_unitaire(self):
        return(self.produit.prix_unitaire)

    def augment_quantite(self,quantite):
        self.quantite += int(quantite)
        self.save()

    def reduire_quantite(self,quantite):
        self.quantite -= quantite
        self.save()

    def get_absolute_url(self):
        return(self.produit.get_absolute_url())

    def delete(self, using=None, keep_parents=False):
        return super().delete(using=using, keep_parents=keep_parents)
    

class DetailCommande(models.Model):
    """
        La classe modèle pour la liste de produits.
    """
    produit = models.ForeignKey(Produit,on_delete=models.CASCADE)
    pu_prod = models.IntegerField(_('PU'),help_text="Prix Unitaire du produit.")
    commande = models.ForeignKey(Commande,on_delete=models.CASCADE)
    quantite = models.IntegerField(_("Quantité"),default=1)
    create_date = models.DateTimeField(_("Date"), auto_now_add=True,help_text="Date de création")
    modified_date = models.DateTimeField(_('Date de modification'), auto_now=True)
    
    class Meta:
        
        verbose_name = 'liste'
        verbose_name_plural = 'listes'
