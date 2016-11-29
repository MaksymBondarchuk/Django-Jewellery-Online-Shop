import os

from django.shortcuts import render
from django.http import HttpRequest

from Lab1.settings import BASE_DIR
from Shop.models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from Shop.forms import OrderForm
from django.http import HttpResponseRedirect
from datetime import datetime
from decimal import Decimal


def create_cart():
    new_cart = Cart()
    new_cart.save()
    cart_id = new_cart.id
    return cart_id


def home(request):
    jewel = Jewel(name='The Daria-e Noor', image='The_Daria-e_Noor_(Sea_of_Light)_Diamond_from_the_collection_of_the_national_jewels_of_Iran_at_Central_Bank_of_Islamic_Republic_of_Iran.jpg', metal_id='583d032ade904f1b6475b931', price=70)
    jewel.save()

    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    try:
        cart_id = request.session["cart_id"]
    except KeyError:
        cart_id = create_cart()
        request.session["cart_id"] = cart_id
    print (os.path.join(BASE_DIR))

    if cart_id is None or Cart.objects.all().filter(id=cart_id).count() == 0:
        cart_id = create_cart()
        request.session["cart_id"] = cart_id

    jewels = Jewel.objects.all()
    # .filter(_id__~Q(id__in=CartItem.objects.all().filter(cart_id=cart_id).values_list("item_id")))

    return render(
        request,
        "index.html",
        {
            "year": datetime.now().year,
            "number_in_cart": CartItem.objects.all().filter(cart_id=cart_id).__len__(),
            "jewels": jewels,
            "metals": Metal.objects.all()
        }
    )


def order(request):
    """Renders the order page."""
    assert isinstance(request, HttpRequest)
    cart_id = request.session["cart_id"]
    cart = Cart.objects.get(pk=cart_id)
    cart_items = CartItem.objects.all().filter(cart_id=cart_id)
    return render(
        request,
        "order.html",
        {
            "year": datetime.now().year,
            "number_in_cart": cart_items.__len__(),
            "cart_items": cart_items,
            "total_price": cart.price_total,
            "form": None
        }
    )


@csrf_exempt
def complete(request):
    # if request.method == "POST":
    form = OrderForm(request.POST)

    cart_id = request.session["cart_id"]
    cart = Cart.objects.get(pk=cart_id)
    cart_items = CartItem.objects.all().filter(cart_id=cart_id)
    if form.is_valid():
        o = Order(name=form.cleaned_data["name"], email=form.cleaned_data["email"],
                  phone=form.cleaned_data["phone"], address=form.cleaned_data["address"],
                  price_total=cart.price_total)
        o.save()

        for cart_item in cart_items:
            oi = OrderItem(order=o, item=Jewel.objects.get(pk=cart_item.item.id), number=cart_item.number)
            oi.save()

        cart.delete()

        return HttpResponseRedirect("/home")

    return render(
        request,
        "order.html",
        {
            "year": datetime.now().year,
            "number_in_cart": cart_items.__len__(),
            "cart_items": cart_items,
            "total_price": cart.price_total,
            "form": form
        }
    )


@csrf_exempt
def buy(request, jewel_id, number):
    assert isinstance(request, HttpRequest)
    cart_id = request.session["cart_id"]
    cart = Cart.objects.get(pk=cart_id)

    added_price = Jewel.objects.get(pk=jewel_id).price * int(number)
    cart_item = CartItem(cart_id=cart_id, item_id=jewel_id, number=number, price=added_price)
    cart_item.save()

    cart.price_total += added_price
    cart.save()

    return HttpResponseRedirect("/")


@csrf_exempt
def remove(request, jewel_id):
    assert isinstance(request, HttpRequest)
    cart_id = request.session["cart_id"]
    CartItem.objects.get(cart_id=cart_id, item_id=jewel_id).delete()
    if CartItem.objects.all().filter(cart_id=cart_id).count() == 0:
        return HttpResponseRedirect("/")
    return HttpResponseRedirect("/order")

