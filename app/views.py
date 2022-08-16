from django.shortcuts import render

from django.http import JsonResponse
from .models import *

def index(request):
    """ Loads index page """
    return render(request, 'app/index.html')

def teaStore(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'app/tea-store.html', context)

def potsStore(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'app/pots-and-sets-store.html', context)

def teawareStore(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'app/teaware-store.html', context)

def basket(request):

    if request.user.is_authenticated:
        customer = request.user
        basket, created = Basket.objects.get_or_create(customer=customer, completedOrder=False)
        items = basket.basketitems_set.all()
    else:
        items = []
        basket = {'get_basket_total': 0, 'get_basket_item': 0}
    
    context = {'items':items, 'basket':basket}
    return render(request, 'app/basket.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        customer_info = CustomerInfo.objects.get(user=customer)
        basket, created = Basket.objects.get_or_create(customer=customer, completedOrder=False)
        items = basket.basketitems_set.all()
    else:
        items = []
        basket = {'get_basket_total': 0, 'get_basket_item': 0}
    
    context = {'items':items, 'basket':basket, 'customer_info':customer_info}
    return render(request, 'app/checkout.html', context)

def updateBasket(request):

    data = json.loads(request.body)
    itemId = data['itemId']
    action = data['addItem']

    print('Item Id:', itemId)
    print('Action:', action)

    customer = request.user
    item = Product.objects.get(id=itemId)
    order, created = Basket.objects.get_or_create(customer=customer, completedOrder=False)

    return JsonResponse('Item added to basket', safe=False)