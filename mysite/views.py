from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    return HttpResponseRedirect("/budget/")
    
