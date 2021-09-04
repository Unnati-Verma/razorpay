from django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length= 1000 , blank=True)
    amount = models.CharField(max_length=100 , blank=True)
    payment_id = models.CharField(max_length=1000 ,blank=True)
    paid = models.BooleanField(default=False)