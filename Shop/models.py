import uuid
from django.db import models


class Metal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Jewel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    metal = models.ForeignKey(Metal, on_delete=models.CASCADE)
    fineness = models.IntegerField(default=0)
    image = models.ImageField(upload_to='Images')
    description = models.CharField(max_length=1000, default='')
    price = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price_total = models.DecimalField(default=0, max_digits=1000, decimal_places=2)


class CartItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Jewel, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    price = models.IntegerField(default=0)


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=False, auto_now=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    price_total = models.DecimalField(default=0, max_digits=1000, decimal_places=2)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Jewel, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.item.name


class CartFilter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    fineness_from = models.IntegerField(null=True)
    fineness_to = models.IntegerField(null=True)
    price_from = models.IntegerField(null=True)
    price_to = models.IntegerField(null=True)
    weight_from = models.IntegerField(null=True)
    weight_to = models.IntegerField(null=True)


class CartMetalFilter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    metal = models.ForeignKey(Metal, on_delete=models.CASCADE)
