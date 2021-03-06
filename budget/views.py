from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.template.defaulttags import register

from collections import OrderedDict
from datetime import date
from datetime import timedelta
import calendar

from .base import *
from .models import *
# Create your views here.
mon_ch2num = {
    "一月": 1,
    "二月": 2,
    "三月": 3,
    "四月": 4,
    "五月": 5,
    "六月": 6,
    "七月": 7,
    "八月": 8,
    "九月": 9,
    "十月": 10,
    "十一月": 11,
    "十二月": 12,
}

@register.filter
def get_dict_item(dictionary, key):
    return dictionary.get(key)

class IndexView(generic.ListView):
    model = Year
    template_name = 'budget/index.html'

    def get_context_data(self, **kwargs):
        
        context = super(IndexView, self).get_context_data(**kwargs)
        context["Year"] = Year.objects.all()
        context["Budget"] = Budget.objects.all()
        context["Bank"] = Bank.objects.all()
        return context 
    
class YearView(generic.ListView):
    model = Year
    template_name = 'budget/year.html'

    def get_context_data(self, **kwargs):
        context = super(YearView, self).get_context_data(**kwargs)
        Year_name = self.kwargs['Year_name']
        year = Year.objects.get(name=Year_name)
        context["year"] = year
        context["Budget"] = Budget.objects.filter(year=year)
        context["Bank"] = Bank.objects.all()
        return context 

class BudgetView(generic.DetailView):

    model = Budget
    template_name = 'budget/budget.html'
    pk_url_kwarg = "Budget_id"
    select_day = date.today()

    def get_context_data(self, **kwargs):
        budget = kwargs['object']
        context = super(BudgetView, self).get_context_data(**kwargs)
        Year_name = self.kwargs['Year_name']
        context["year"] = Year.objects.get(name=Year_name)
        context["Bank"] = Bank.objects.all()
        context["Deposit"] = budget.deposit_set.all()
        ratio = 0.3
        context["LivingCost"] = LivingCost.objects.get_or_create(
                name="生活/娛樂費", 
                ratio=ratio, 
                budget=budget)[0]
        ratio = 0.1
        context["BackupCost"] = LivingCost.objects.get_or_create(
                name="備用", 
                ratio=ratio, 
                budget=budget)[0]
        context["Incomes"] = budget.incomes_set.all().order_by('date')
        context["Expenses"] = budget.expenses_set.all().order_by('date')
        choices = OrderedDict()
        for c_id, c_name in CHOICES:
            choices[c_name] = 0
            for e in budget.expenses_set.filter(category=c_id, is_fulfill=True):
                choices[c_name] += e.value
        context["CHOICES"] = choices
        context["Today"] = date.today()
        select_day_list = [self.select_day]
        day_range = 2
        for i in range(1, day_range+1):
            select_day_list.append(self.select_day-timedelta(days=i))
            select_day_list.append(self.select_day+timedelta(days=i))
        select_day_list.sort()
        context["DAY_LIST"] = select_day_list 
        max_date = calendar.monthrange(int(Year_name), mon_ch2num[budget.name])[1]
        
        return context

    
def add_debt(request, Year_name, Budget_id):
    
    Debt_name = request.GET["Debt_name"]
    value = request.GET["value"]
    Category_name = request.GET["Category_name"]
    
    B = Budget.objects.get(id=Budget_id)
    for k, v in dict(CHOICES).items():
        if v == Category_name:
            category = k
    debt = Debt(name=Debt_name, value=value, remain=value, budget=B, category=category)
    debt.save()
    return HttpResponseRedirect('/budget/{}/{}'.format(Year_name, Budget_id)) 

def pay_debt(request, Year_name, Budget_id):

    Debt_id = request.GET["Debt_id"]
    budget = Budget.objects.get(id=Budget_id)
    debt = Debt.objects.get(id=Debt_id, budget=budget)
    debt.is_paid = True
    for ex in debt.expenses.all():
        ex.is_fulfill = True
        ex.save()
    debt.save()
    return HttpResponseRedirect('/budget/{}/{}'.format(Year_name, Budget_id)) 

def delete_item(request, Year_name, Budget_id):
    
    Item_id = request.GET['Item_id']
    I = Item.objects.get(id=Item_id)
    I.delete()
    return HttpResponseRedirect('/budget/{}/{}'.format(Year_name, Budget_id)) 

def add_income(request, Year_name, Budget_id):
    
    name = request.GET["name"] 
    value = request.GET["value"]
    date = request.GET["date"]
    Bank_name = request.GET["Bank_name"]

    budget = Budget.objects.get(id=Budget_id)
    bank = Bank.objects.get(name=Bank_name)

    value = int(value.replace(',', ''))
    income_remain = value
    
    for debt in Debt.objects.filter(budget=budget):
        if not debt.is_paid:
            if debt.remain > income_remain:
                ex_value = income_remain
                debt.remain -= income_remain
                remain = 0
            else:
                ex_value = debt.remain
                income_remain -= debt.remain
                debt.remain = 0
                debt.is_distributed = True
            belong_to = debt
            expense = Expenses(
                    name="償還_{}".format(debt.name), 
                    value=ex_value, 
                    date=date, 
                    bank=bank, 
                    belong_to=belong_to, 
                    category=debt.category,
                    budget=budget, 
                    is_fulfill=False)
            debt.save()
            expense.save() 

    bank.value += income_remain
    bank.save()
    
    income = Incomes(
            name=name, 
            value=value, 
            remain=income_remain, 
            date=date, 
            bank=bank, 
            budget=budget)
    income.save() 

    ratio = 0.6
    D = Deposit(name="存款_{}".format(name), ratio=ratio, budget=budget, income=income)
    D.update()
    D.save()

    LC = LivingCost.objects.get(name="生活/娛樂費", budget=budget)
    LC.update()
    LC.save()

    BC = LivingCost.objects.get(name="備用" ,budget=budget)
    BC.update()
    BC.save()

    return HttpResponseRedirect('/budget/{}/{}'.format(Year_name, Budget_id)) 

def add_expense(request, Year_name, Budget_id):
    
    name = request.GET["name"] 
    value = int(request.GET["value"])
    date = request.GET["date"]
    print(date)
    Bank_name = request.GET["Bank_name"]
    Category_name = request.GET["Category_name"]

    bank = Bank.objects.get(name=Bank_name)
    budget = Budget.objects.get(id=Budget_id)
    LC = LivingCost.objects.get(name="生活/娛樂費", budget=budget)
    BC = LivingCost.objects.get(name="備用", budget=budget)
    bank.value -= value
    bank.save()
    if(LC.remain >= value):
        belong_to = LC
        LC.remain -= value
    else:
        belong_to = BC
        BC.remain -= value
    for k, v in dict(CHOICES).items():
        if v == Category_name:
            category = k
    expense = Expenses(
            name=name, 
            value=value, 
            date=date, 
            bank=bank, 
            belong_to=belong_to, 
            category=category, 
            budget=budget, 
            is_fulfill=True)
    expense.save() 
    BC.update()
    LC.update()
    BC.save()
    LC.save()
    return HttpResponseRedirect('/budget/{}/{}'.format(Year_name, Budget_id)) 

def show_prev_ex(request, Year_name, Budget_id):
    BudgetView.select_day-=timedelta(days=2)
    print(BudgetView.select_day)
    data = {'a': 1}
    return JsonResponse(data)
    


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
    
