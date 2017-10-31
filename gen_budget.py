from budget.models import *
import datetime
year = 2017
months = ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]

for idx, month in enumerate(months):
    date = datetime.date(year=year, month=idx+1, day=1)
    B = Budget(name=month, date=date)
    B.save()
    Item(name="孝親費",         value=10000, remain=10000, budget=B).save()
    Item(name="定存",           value=20000, remain=20000, budget=B).save()
    Item(name="投資",           value=15000, remain=15000, budget=B).save()
    Item(name="公司花費(自助)", value=2500,  remain=2500,  budget=B).save()
    Item(name="生活費",         value=12500, remain=12500, budget=B).save()
    Item(name="房租",           value=16000, remain=16000, budget=B).save()

