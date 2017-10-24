from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse

from .models import Budget, Item, Bank, Investment, Transactions
# Create your views here.
class IndexView(generic.ListView):

    template_name = 'budget/index.html'
    context_object_name = 'Budget'

    def get_queryset(self):
        
        return Budget.objects.all()
    
    def get_context_data(self, **kwargs):
        
        context = super(IndexView, self).get_context_data(**kwargs)
        context["Bank"] = Bank.objects.all()
        context["Transactions"] = Bank.objects.all()
        return context
    
    def add_item(self):
        
        Budget_name = self.GET["Budget_name"]
        Item_name = self.GET["Item_name"]
        value = self.GET["value"]
        Item(name = Item_name)
        
        B = Budget.objects.get(name=Budget_name)
        I = Item(name=Item_name, value=value, remain=value, budget=B)
        I.save()
        return HttpResponseRedirect('/budget/') 

    def delete_item(self):
        
        Item_id = self.GET['Item_id']
        I = Item.objects.get(id=Item_id)
        I.delete()
        return HttpResponseRedirect('/budget/') 

