# Create your models here.
from django.db import models

# list of stocks to retreive prices for
class Retreive(models.Model):
    symbol = models.CharField(max_length=20)

    def __str__(self):
        return self.symbol

class Price(models.Model):
    symbol = models.CharField(max_length=20, db_index=True)
    datetime = models.DateTimeField(db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)

    def __str__(self):
        return f"{self.symbol} - {self.datetime} - {self.price}"