from budget.models import *
import datetime
months = ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]

for y in range(2018, 2020):
    year = Year(name=y)
    year.save()
    for m in months:
        B = Budget(name=m)
        B.year=year
        B.save()
#  print(LC[0].value)
#  LC[0].save()
#  LC = LivingCost.objects.get(budget=budget)
#  print(LC)
#  i = Incomes.objects.get(name="聯發科10月薪資").delete()
#  i = Incomes.objects.get(name="內政部11月薪資").delete()
