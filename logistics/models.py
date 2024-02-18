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


class Package(models.Model):
    PENDING = 'created'
    ASSIGNED = 'assigned'
    DELIVERED = 'delivered'

    STATUS_CHOICES = [
        (PENDING, 'Created'),
        (ASSIGNED, 'Assigned'),
        (DELIVERED, 'Delivered'),
    ]

    id = models.CharField(max_length=128, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    dimensions = models.CharField(max_length=32)
    weight = models.CharField(max_length=32)
    destination_address = models.CharField(max_length=32)
    origin_address = models.CharField(max_length=32)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)

    # Foreing Keys
    assigned_courier = models.ForeignKey(Courier, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_packages')
    sender = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sent_packages')

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

