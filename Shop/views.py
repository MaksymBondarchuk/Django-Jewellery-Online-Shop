from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from Shop.models import Metal, Jewel


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
            'numberInCard': 45,
            'jewels': Jewel.objects.all()
        }
    )
