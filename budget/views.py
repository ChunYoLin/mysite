from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.template.defaulttags import register

from collections import OrderedDict

from .base import *
from .models import *
# Create your views here.

@register.filter
def get_dict_item(dictionary, key):
    return dictionary.get(key)

class IndexView(generic.ListView):

    model = Budget
    template_name = 'budget/index.html'

    def get_context_data(self, **kwargs):
        
        context = super(IndexView, self).get_context_data(**kwargs)
        context["Budget"] = Budget.objects.all()
        context["Bank"] = Bank.objects.all()
        return context 
    
class DetailView(generic.DetailView):

    model = Budget
    template_name = 'budget/detail.html'
    

    def get_context_data(self, **kwargs):
        budget = kwargs['object']
        context = super(DetailView, self).get_context_data(**kwargs)
        context["Bank"] = Bank.objects.all()
        context["Deposit"] = budget.deposit_set.all()
        context["BackupCost"] = budget.backupcost_set.all()
        context["LivingCost"] = budget.livingcost_set.all()
        context["Incomes"] = budget.incomes_set.all().order_by('date')
        context["Expenses"] = budget.expenses_set.all().order_by('date')
        choices = OrderedDict()
        for c_id, c_name in CHOICES:
            choices[c_name] = 0
            for e in budget.expenses_set.filter(category=c_id):
                choices[c_name] += e.value
        context["CHOICES"] = choices
            
        
        return context
    
    def add_debt(self, pk):
        
        Budget_name = self.GET["Budget_name"]
        Debt_name = self.GET["Debt_name"]
        value = self.GET["value"]
        
        B = Budget.objects.get(name=Budget_name)
        debt = Debt(name=Debt_name, value=value, remain=value, budget=B)
        debt.save()
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

    budget = Budget.objects.get(id=Budget_id)
    value = int(value.replace(',', ''))
    remain = value
    
    for debt in Debt.objects.all():
        if not debt.is_paid:
            if debt.remain > remain:
                debt.remain -= remain
                remain = 0
            else:
                remain -= debt.remain
                debt.remain = 0
                debt.is_paid = True
            debt.save()

    bank = Bank.objects.get(name=Bank_name)
    bank.value += remain
    bank.save()
    
    income = Incomes(name=name, value=value, remain=remain, date=date, bank=bank, budget=budget)
    income.save() 

    ratio = 0.6
    D = Deposit(name="存款_{}".format(name), ratio=ratio, budget=budget, income=income)
    D.update()
    D.save()

    ratio = 0.3
    LC = LivingCost.objects.get_or_create(name="生活/娛樂費", ratio=ratio, budget=budget)[0]
    LC.update()
    LC.save()

    ratio = 0.1
    LC = LivingCost.objects.get_or_create(name="備用", ratio=ratio, budget=budget)[0]
    LC.update()
    LC.save()

    return HttpResponseRedirect('/budget/{}/'.format(Budget_id)) 

def add_expense(request, Budget_id):
    
    name = request.GET["name"] 
    value = request.GET["value"]
    date = request.GET["date"]
    Bank_name = request.GET["Bank_name"]
    Item_name = request.GET["Item_name"]

    bank = Bank.objects.get(name=Bank_name)
    budget = Budget.objects.get(id=Budget_id)
    item = LivingCost.objects.get(name=Item_name, budget=budget)
    bank.value -= int(value)
    bank.save()
    item.remain -= int(value)
    item.save()
    expense = Expenses(name=name, value=value, date=date, bank=bank, item=item, budget=budget)
    expense.save() 
    return HttpResponseRedirect('/budget/{}/'.format(Budget_id)) 

def asset_transfer(request):
    
    try:
        bank_src_name = request.POST["bank_src"]
        value = int(request.POST["value"])
        bank_dst_name = request.POST["bank_dst"]
    except ValueError:
        return HttpResponseRedirect('/budget/') 

    bank_src = Bank.objects.get(name=bank_src_name)
    bank_dst = Bank.objects.get(name=bank_dst_name)
    if bank_src.value < value or value < 0:
        pass
    else:
        bank_src.value -= value
        bank_src.save()
        bank_dst.value += value
        bank_dst.save()
    return HttpResponseRedirect('/budget/') 
    
