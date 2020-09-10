from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.contrib.auth.models import User

class HomeView(ListView):
    
    ctx={}
    model=User
    template_name='AkunaApp/index.html'

    def get_context_data(self,**kwargs):
        self.ctx= super(HomeView,self).get_context_data(**kwargs)    
        return(self.ctx)
        
    def get_queryset(self):
        return super().get_queryset()

    def get_template_names(self):
        return super().get_template_names()

class ProductDetailView(DetailView):
    pass
