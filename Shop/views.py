from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from Shop.models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from Shop.forms import OrderForm
from django.http import HttpResponseRedirect
from datetime import datetime
from decimal import Decimal
from django import template

register = template.Library()


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    try:
        cart_id = request.session['cart_id']
    except KeyError:
        new_cart = Cart()
        new_cart.save()
        cart_id = new_cart.id
        request.session['cart_id'] = cart_id.hex

        cart_filter = CartFilter(cart_id=cart_id)
        cart_filter.save()
    # cart = Cart.objects.get(pk=cart_id)
    jewels = Jewel.objects.all().filter(
        ~Q(id__in=CartItem.objects.all().filter(cart_id=cart_id).values_list('item_id')))

    # Metal filter
    cart_metal_filter = CartMetalFilter.objects.all().filter(cart_id=cart_id)
    if cart_metal_filter:
        jewels = jewels.filter(metal__id__in=cart_metal_filter.values_list('metal_id'))

    # Other filters
    cart_filter = CartFilter.objects.all().filter(cart_id=cart_id).first()
    if cart_filter.fineness_from is not None:
        jewels = jewels.filter(fineness__gte=cart_filter.fineness_from)
    if cart_filter.fineness_to is not None:
        jewels = jewels.filter(fineness__lte=cart_filter.fineness_to)

    if cart_filter.price_from is not None:
        jewels = jewels.filter(price__gte=cart_filter.price_from)
    if cart_filter.price_to is not None:
        jewels = jewels.filter(price__lte=cart_filter.price_to)

    if cart_filter.weight_from is not None:
        jewels = jewels.filter(weight__gte=cart_filter.weight_from)
    if cart_filter.weight_to is not None:
        jewels = jewels.filter(weight__lte=cart_filter.weight_to)

    return render(
        request,
        'index.html',
        {
            'year': datetime.now().year,
            'number_in_cart': CartItem.objects.all().filter(cart_id=cart_id).__len__(),
            'jewels': jewels,
            'metals': Metal.objects.all(),
            'filtered_metals': cart_metal_filter.values_list('metal_id', flat=True),
            'fineness_from': cart_filter.fineness_from if cart_filter.fineness_from is not None else '',
            'fineness_to': cart_filter.fineness_to if cart_filter.fineness_to is not None else '',
            'price_from': cart_filter.price_from if cart_filter.price_from is not None else '',
            'price_to': cart_filter.price_to if cart_filter.price_to is not None else '',
            'weight_from': cart_filter.weight_from if cart_filter.weight_from is not None else '',
            'weight_to': cart_filter.weight_to if cart_filter.weight_to is not None else '',
        }
    )


def order(request):
    """Renders the order page."""
    assert isinstance(request, HttpRequest)
    form = OrderForm(request.POST)
    cart_id = request.session['cart_id']
    return render(
        request,
        'order.html',
        {
            'year': datetime.now().year,
            'number_in_cart': CartItem.objects.all().filter(cart_id=cart_id).__len__(),
            'cart_items': CartItem.objects.all().filter(cart_id=cart_id)
        },
    )


@csrf_exempt
def complete(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            global cart, filtered_metals, fineness_from, fineness_to

            o = Order(name=form.cleaned_data['name'], email=form.cleaned_data['email'],
                      phone=form.cleaned_data['phone'], address=form.cleaned_data['address'])
            o.save()

            for item in cart:
                oi = OrderItem(order=o, item=Jewel.objects.get(pk=item))
                oi.save()

            cart = []
            filtered_metals = []
            fineness_from = None
            fineness_to = None

            return HttpResponseRedirect('/home')

    return render(
        request,
        'order.html',
        {
            'year': datetime.now().year,
            'number_in_cart': cart.__len__(),
            'jewels': Jewel.objects.all().filter(id__in=cart)
        },
    )


@csrf_exempt
def buy(request, jewel_id, number):
    assert isinstance(request, HttpRequest)
    cart_id = request.session['cart_id']

    jewel = Jewel.objects.get(pk=jewel_id)
    cart_item = CartItem(cart_id=cart_id, item_id=jewel_id, number=number, price=jewel.price*int(number))
    cart_item.save()

    return HttpResponseRedirect('/')


@csrf_exempt
def remove(request, jewel_id):
    assert isinstance(request, HttpRequest)
    cart_id = request.session['cart_id']
    CartItem.objects.get(cart_id=cart_id, item_id=jewel_id).delete()
    if CartItem.objects.all().filter(cart_id=cart_id).count() == 0:
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/order')


@csrf_exempt
def metal(request, metal_id, is_for_add):
    cart_id = request.session['cart_id']
    if is_for_add == 'true':
        cart_metal_filter = CartMetalFilter(cart_id=cart_id, metal_id=metal_id)
        cart_metal_filter.save()
    else:
        CartMetalFilter.objects.all().filter(cart_id=cart_id).filter(metal_id=metal_id).delete()
    return HttpResponseRedirect('/')


@csrf_exempt
def update_filter(request, parameter, from_to, value):
    assert isinstance(request, HttpRequest)

    cart_id = request.session['cart_id']
    cart_filter = CartFilter.objects.get(cart_id=cart_id)
    if parameter == 'fineness':
        if from_to == 'from':
            cart_filter.fineness_from = int(value) if value != '-1' else None
        else:
            cart_filter.fineness_to = int(value) if value != '-1' else None
    elif parameter == 'price':
        if from_to == 'from':
            cart_filter.price_from = Decimal(value) if value != '-1' else None
        else:
            cart_filter.price_to = Decimal(value) if value != '-1' else None
    elif parameter == 'weight':
        if from_to == 'from':
            cart_filter.weight_from = int(value) if value != '-1' else None
        else:
            cart_filter.weight_to = int(value) if value != '-1' else None
    cart_filter.save()

    return HttpResponseRedirect('/')


@register.filter
def div(value, arg):
    return int(value) * int(arg)
