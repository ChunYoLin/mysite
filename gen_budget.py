from budget.models import *
import datetime
months = ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]

year = Year.objects.get(name=2017)
budget = Budget.objects.get(name="十一月", year=year)
LC = LivingCost.objects.get(name="生活/娛樂費", budget=budget)
BC = LivingCost.objects.get(name="備用", budget=budget)
#  for ex in Expenses.objects.filter(date__range=[datetime.datetime(2017,11,20), datetime.datetime(2017,11,23)], budget=budget):
    #  ex.belong_to = BC
    #  ex.save()

for ex in Expenses.objects.all():
    ex.is_fulfill = True
    ex.save()
#  print(LC[0].value)
#  LC[0].save()
#  LC = LivingCost.objects.get(budget=budget)
#  print(LC)
#  i = Incomes.objects.get(name="聯發科10月薪資").delete()
#  i = Incomes.objects.get(name="內政部11月薪資").delete()
