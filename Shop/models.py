from django.db import models
from django_mongodb_engine.contrib import MongoDBManager
from djangotoolbox.fields import ListField, EmbeddedModelField


class Metal(models.Model):
    created_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    objects = MongoDBManager()


class Jewel(models.Model):
    created_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    name = models.CharField(max_length=100)
    metal = models.ForeignKey(Metal, on_delete=models.CASCADE)
    fineness = models.IntegerField(default=0)
    image = models.ImageField(upload_to='../Images/')
    description = models.CharField(max_length=1000, default='')
    price = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    objects = MongoDBManager()


class Cart(models.Model):
    created_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    price_total = models.IntegerField(default=0)

    # items = ListField(EmbeddedModelField('CartItem'))

    objects = MongoDBManager()


class CartItem(models.Model):
    created_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Jewel, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    price = models.IntegerField(default=0)

    objects = MongoDBManager()


class Order(models.Model):
    created_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    price_total = models.DecimalField(default=0, max_digits=1000, decimal_places=2)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    objects = MongoDBManager()


class OrderItem(models.Model):
    created_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Jewel, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)

    def __unicode__(self):
        return self.item.name

    objects = MongoDBManager()
