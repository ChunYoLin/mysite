from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse

from budget.models import Budget, Item, Bank, Investment, Transactions

class IndexView(generic.ListView):

    template_name = 'mysite/index.html'
    context_object_name = 'Budget'

    def get_queryset(self):
        return Budget.objects.all()
