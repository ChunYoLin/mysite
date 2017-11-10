from budget.models import *
import datetime
year = 2017
months = ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]

B = Budget.objects.get(name="十一月")
incomes = Incomes.objects.filter(budget=B)
print(Deposit.objects.all().delete())

for I in incomes:
    v = int(I.remain * 0.7)
    name = "存款_{}".format(I.name)
    D = Deposit(name=name, value = v, budget=B)
    D.save()
    print(name)
    print(v)
#  for idx, month in enumerate(months):
    #  B = Budget.objects.get(name=month)
    #  #  Item(name="孝親費",         value=10000, remain=10000, budget=B).save()
    #  #  Item(name="定存",           value=20000, remain=20000, budget=B).save()
    #  #  Item(name="投資",           value=15000, remain=15000, budget=B).save()
    #  #  Item(name="公司花費(自助)", value=2500,  remain=2500,  budget=B).save()
    #  #  Item(name="生活費",         value=12500, remain=12500, budget=B).save()
    #  #  Item(name="房租",           value=16000, remain=16000, budget=B).save()
    #  Debt(name="孝親費", value=10000, budget=B, is_paid=False).save()
    #  Debt(name="房租",   value=12500, budget=B, is_paid=False).save()
    
    #  Deposit(name="存款", ratio=70, is_paid=False, budget=B).save()
    #  LivingCost(name="生活費", ratio=30).save()

