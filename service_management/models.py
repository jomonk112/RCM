from django.db import models

import uuid

class Brands(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand_name = models.CharField(max_length=100, unique=True)


class Coupons(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.ForeignKey(Brands, related_name='brand',on_delete=models.CASCADE)
    code = models.CharField(max_length=100, unique=True)
    value = models.IntegerField()
