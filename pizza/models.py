from django.db import models

# Create your models here.

class Topping(models.Model):
    name = models.CharField(max_length=200)
    # quantity = models.IntegerField(default=0)

class Pizza(models.Model):
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    toppings = models.ManyToManyField(Topping)