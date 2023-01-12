from django.shortcuts import render
from .models import changes
from django.db.models import Sum
# Create your views here.


def submit_buy(request):
    a = request.GET
    if a == {}:
        context = 'choose rate!!!!!'
    else:
        context = changes.objects.filter(rate = a['rate'])
    return render(request,template_name= 'filter.html',context={'sum':context})


def home(request):
    return render(request,template_name= 'home.html')