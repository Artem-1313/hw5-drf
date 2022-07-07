from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=800)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

