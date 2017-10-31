from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse

from .models import Budget, Item, Bank, Investment, Incomes, Expenses
# Create your views here.
class IndexView(generic.ListView):

    template_name = 'budget/index.html'
    context_object_name = 'Budget'

    def get_queryset(self):
        
        return Budget.objects.all()
    
class DetailView(generic.DetailView):

    model = Budget
    template_name = 'budget/detail.html'

    def get_context_data(self, **kwargs):
        B = kwargs['object']
        context = super(DetailView, self).get_context_data(**kwargs)
        context["Bank"] = Bank.objects.all()
        context["Incomes"] = B.incomes_set.all()
        context["Expenses"] = B.expenses_set.all()
        
        return context
    
    def add_item(self, pk):
        
        Budget_name = self.GET["Budget_name"]
        Item_name = self.GET["Item_name"]
        value = self.GET["value"]
        Item(name = Item_name)
        
        B = Budget.objects.get(name=Budget_name)
        I = Item(name=Item_name, value=value, remain=value, budget=B)
        I.save()
        return HttpResponseRedirect('/budget/{}'.format(pk)) 

    def delete_item(self, pk):
        
        Item_id = self.GET['Item_id']
        I = Item.objects.get(id=Item_id)
        I.delete()
        return HttpResponseRedirect('/budget/{}'.format(pk)) 

def add_income(request, Budget_id):
    
    name = request.GET["name"] 
    value = request.GET["value"]
    date = request.GET["date"]
    Bank_name = request.GET["Bank_name"]

    bank = Bank.objects.get(name=Bank_name)
    budget = Budget.objects.get(id=Budget_id)
    bank.value += int(value)
    bank.save()
    income = Incomes(name=name, value=value, date=date, bank=bank, budget=budget)
    income.save() 
    return HttpResponseRedirect('/budget/{}/'.format(Budget_id)) 

def add_expense(request, Budget_id):
    
    name = request.GET["name"] 
    value = request.GET["value"]
    date = request.GET["date"]
    Bank_name = request.GET["Bank_name"]
    Item_name = request.GET["Item_name"]

    bank = Bank.objects.get(name=Bank_name)
    budget = Budget.objects.get(id=Budget_id)
    item = Item.objects.get(name=Item_name, budget=budget)
    bank.value -= int(value)
    bank.save()
    item.remain -= int(value)
    item.save()
    expense = Expenses(name=name, value=value, date=date, bank=bank, item=item, budget=budget)
    expense.save() 
    return HttpResponseRedirect('/budget/{}/'.format(Budget_id)) 
