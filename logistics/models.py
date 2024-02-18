from django.db import models
import uuid

class Customer(models.Model):
    id = models.CharField(max_length=128, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    fullname = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    phone = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.fullname)

    class Meta:
        ordering = ['fullname']


class Courier(models.Model):
    id = models.CharField(max_length=128, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
