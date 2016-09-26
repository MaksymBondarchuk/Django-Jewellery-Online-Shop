import uuid
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from Shop.models import Metal, Jewel
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

card = []
filtered_metals = []


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    jewels = Jewel.objects.all().filter(~Q(id__in=card))
    if filtered_metals.__len__() > 0:
        jewels = jewels.filter(metal__id__in=filtered_metals)
    return render(
        request,
        'index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
            'numberInCard': card.__len__(),
            'jewels': jewels,
            'metals': Metal.objects.all(),
            'forbidden_metals': filtered_metals
        },
    )


def order(request):
    """Renders the order page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'order.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
            'numberInCard': card.__len__(),
            'jewels': Jewel.objects.all().filter(id__in=card)
        },
    )


@csrf_exempt
def buy(request):
    assert isinstance(request, HttpRequest)
    jewel_id = request.POST.get('jewel', '')
    card.append(jewel_id)
    return render(
        request,
        'index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
            'numberInCard': card.__len__(),
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
            'title': 'Home Page',
            'year': datetime.now().year,
            'numberInCard': card.__len__(),
            'jewels': Jewel.objects.all()
        },
        RequestContext(request)
    )
