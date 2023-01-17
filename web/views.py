from django.shortcuts import render
from .models import buy , orders , changes
from django.db.models import Sum
# Create your views here.

def remained(oredrID):
    this_order = orders.objects.filter(followCode = oredrID).get()
    buys = buy.objects.filter(order = this_order)
    lirs = changes.objects.filter(order = this_order).aggregate(Sum('lir'))
    mande = lirs['lir__sum']
    for x in buys:
        mande -= (x.sud)+ (x.amount)

    return mande

def submit_buy(request):
    context = {}
    a = request.GET
    if a == {}:
        context = {}
    else:
        this_id = a['rate']
        this_order = orders.objects.filter(followCode = this_id).get()
        context['sum'] = changes.objects.filter(order = this_order)
        context['mande'] = remained(this_id)
    return render(request,template_name= 'filter.html',context=context)


def home(request):
    return render(request,template_name= 'home.html')