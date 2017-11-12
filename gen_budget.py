from budget.models import *
import datetime
year = 2017
months = ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]
budget = Budget.objects.get(name="十一月")
income = Deposit.objects.get(name="存款_內政部12月薪資")
income.name = "存款_內政部11月薪資"
income.save()
#  for income in incomes:
    #  LC.value += int(income.remain*0.3)
#  LC = LivingCost.objects.get(budget=budget)
#  print(LC)
#  i = Incomes.objects.get(name="聯發科10月薪資").delete()
#  i = Incomes.objects.get(name="內政部11月薪資").delete()
