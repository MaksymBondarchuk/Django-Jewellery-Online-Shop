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

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
