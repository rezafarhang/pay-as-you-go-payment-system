from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

choices = (
        ("pors", "pors"),
        ("line", "line")
    )

class Price(models.Model):
    unit_price = models.DecimalField(max_digits=10 ,decimal_places=4)
    service_name = models.CharField(max_length=255, choices=choices)
    created_at = models.DateTimeField(auto_now_add=True)


class Cost(models.Model):
    request_cost = models.DecimalField(max_digits=10 ,decimal_places=4)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=255)

