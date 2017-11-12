from budget.models import *
import datetime
year = 2017
months = ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]
budget = Budget.objects.get(name="十一月")
LC = LivingCost.objects.get(name="生活費", budget=budget)
I = Incomes.objects.filter(budget=budget)
LC.ratio = 40
LC.save()
#  for income in incomes:
    #  LC.value += int(income.remain*0.3)
#  LC = LivingCost.objects.get(budget=budget)
#  print(LC)
#  i = Incomes.objects.get(name="聯發科10月薪資").delete()
#  i = Incomes.objects.get(name="內政部11月薪資").delete()
