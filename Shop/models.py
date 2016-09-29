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
    image = models.CharField(max_length=250)
    description = models.CharField(max_length=1000, default='')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True, blank=True)

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
