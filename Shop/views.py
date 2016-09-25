from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from Shop.models import Metal, Jewel
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q


card = []


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
            'numberInCard': card.__len__(),
            'jewels': Jewel.objects.all().filter(~Q(id__in=card))
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
