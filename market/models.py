from django.db import models
from django.core.validators import  MinValueValidator
# Create your models here.

class Order(models.Model):
    side_option = [
        ('buy', 'buy'),
        ('sell', 'sell'),
    ]

    isin = models.CharField(max_length=12,  primary_key=True)
    limit_price = models.FloatField(
        validators=[MinValueValidator(1)],
                                    )
    side = models.CharField(choices=side_option, max_length=4)
    valid_until = models.IntegerField(
         validators=[MinValueValidator(1)],
                                    )
    quantity = models.PositiveIntegerField(
         validators=[MinValueValidator(1)],
                                        )
