from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Year)
admin.site.register(Budget)
admin.site.register(Debt)
admin.site.register(Deposit)
admin.site.register(LivingCost)
admin.site.register(BackupCost)
admin.site.register(Bank)
admin.site.register(Incomes)
admin.site.register(Expenses)

class LivingCostAdmin(admin.ModelAdmin):
    list_display = ('ratio', 'value', 'remain', 'budget', 'category')
