from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from Shop.models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from Shop.forms import OrderForm
from django.http import HttpResponseRedirect
from datetime import datetime


cart = []
filtered_metals = []
fineness_from = None
fineness_to = None


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    jewels = Jewel.objects.all().filter(~Q(id__in=cart))
    if filtered_metals:
        jewels = jewels.filter(metal__id__in=filtered_metals)
    if fineness_from is not None:
        jewels = jewels.filter(fineness__gte=fineness_from)
    if fineness_to is not None:
        jewels = jewels.filter(fineness__lte=fineness_to)
    return render(
        request,
        'index.html',
        {
            'year': datetime.now().year,
            'number_in_cart': cart.__len__(),
            'jewels': jewels,
            'metals': Metal.objects.all(),
            'forbidden_metals': filtered_metals,
            'fineness_from': fineness_from if fineness_from is not None else '',
            'fineness_to': fineness_to if fineness_to is not None else ''
        },
    )


def order(request):
    """Renders the order page."""
    assert isinstance(request, HttpRequest)
    form = OrderForm(request.POST)
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
def complete(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            global cart, filtered_metals, fineness_from, fineness_to

            o = Order(name=form.cleaned_data['name'], email=form.cleaned_data['email'],
                      phone=form.cleaned_data['phone'], address=form.cleaned_data['address'],)
                      # session=uuid.UUID(request.session))
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
def buy(request):
    assert isinstance(request, HttpRequest)
    jewel_id = uuid.UUID(request.POST.get('jewel', ''))
    cart.append(jewel_id)
    return render(
        request,
        'index.html',
        {
            'year': datetime.now().year,
            'numberInCard': cart.__len__(),
            'jewels': Jewel.objects.all()
        },
        RequestContext(request)
    )


@csrf_exempt
def remove(request):
    assert isinstance(request, HttpRequest)
    jewel_id = request.POST.get('jewel', '')
    cart.remove(jewel_id)
    return render(
        request,
        'index.html',
        {
            'year': datetime.now().year,
            'numberInCard': cart.__len__(),
            'jewels': Jewel.objects.all()
        },
        RequestContext(request)
    )


@csrf_exempt
def metal(request):
    assert isinstance(request, HttpRequest)
    metal_id = uuid.UUID(request.POST.get('metal', ''))
    state = request.POST.get('state', '')
    if state != 'false':
        filtered_metals.append(metal_id)
    else:
        filtered_metals.remove(metal_id)
    return render(
        request,
        'index.html',
        {
            'year': datetime.now().year,
            'numberInCard': cart.__len__(),
            'jewels': Jewel.objects.all()
        },
        RequestContext(request)
    )


@csrf_exempt
def fineness(request):
    assert isinstance(request, HttpRequest)
    parameter = request.POST.get('parameter', '')
    value = request.POST.get('value', '')
    if value == '':
        value = None
    else:
        value = int(value)
    if parameter == 'from':
        global fineness_from
        fineness_from = value
    else:
        global fineness_to
        fineness_to = value
    return render(
        request,
        'index.html',
        {
            'year': datetime.now().year,
            'numberInCard': cart.__len__(),
            'jewels': Jewel.objects.all()
        },
        RequestContext(request)
    )
