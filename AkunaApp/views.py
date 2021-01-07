from django.views.generic.list import ListView
from django.views.generic import DetailView,TemplateView,View
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.core.exceptions import ValidationError,ObjectDoesNotExist
from django.shortcuts import Http404

from .models import Produit,Categorie,PanierModel,PanierElementModel
import json

class HomeView(ListView):
    
    ctx={}
    model = Produit
    template_name='AkunaApp/index.html'

    def get_context_data(self,**kwargs):
        
        self.ctx= super(HomeView,self).get_context_data(**kwargs)
        try:
            categories = Categorie.objects.all()
        except ObjectDoesNotExist as e:
            return(Http404())
        self.ctx["categories"]=categories
        return(self.ctx)
        
    def get_queryset(self):
        return super().get_queryset()

    def get_template_names(self):
        return super().get_template_names()
    

class ProduitDetailView(DetailView):
    model = Produit
    template_name ='AkunaApp/detail.html'
    # queryset = PanierElementModel.obejects.all()

class CartDetailView(ListView):
    template_name = "AkunaApp/cart.html"
    model = PanierElementModel
    def get_context_data(self, **kwargs):
        context = super(CartDetailView,self).get_context_data(**kwargs)
        if(self.request.user.is_authenticated):
            pass
        else:
            cookie_cart = json.loads(self.request.COOKIES['cart'])
        try:
            cart = PanierModel.objects.get(pk=int(cookie_cart['id']))
        except ObjectDoesNotExist as e:
            print(e)
        self.queryset = self.get_queryset().filter(panier=cart)
        context['panier_elts'] = self.get_queryset()
        return(context)
    
    def delete(self,*args, **kwargs):
        pass
    
    def get_queryset(self):
        return super().get_queryset()
    
    

class AnnonymousPanierJsonView(View):

    def get(self,*args,**wargs):
        if(self.request.is_ajax()):
            if(self.request.GET.get('action')=='create_cart'):
                cart = PanierModel()
                cart.save() #Ecrire un signal qui va surveillé cet objet pour qu'il soit suprimé apres 2 semaines
                return(JsonResponse(cart.id,safe=False))
        return(JsonResponse(None,safe=False))

    
    def post(self,*args,**kwargs):
        if(self.request.is_ajax()):
            action = self.request.POST.get('action')
            cart_id = self.request.POST.get('cart')
            if(action=="add_Item"):
                cart_id = int(cart_id)
                cart = PanierModel.objects.get(pk=cart_id)

                product_id = self.request.POST.get('produit')
                product_id = int(product_id)
                produit = Produit.objects.get(pk=product_id)
                cart_item = PanierElementModel(panier=cart,produit=produit)
                cart_item.save()
                return(JsonResponse(cart_item.produit.id,safe=False))
            elif(action == "del_Item"):
                pass
            elif(action == "del_all"):
                pass
            else:
                pass

            
        else:
            print(self.request.POST)

    def put(self,request,old_data,new_data,*args,**kwargs):
        """
        La méthode de modification d'une détail la commande
        """
        pass

    def delete(self,data,args):
        """
        La méthode de suppression de contenu du panier.
        """
        pass
