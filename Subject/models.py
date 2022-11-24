from django.db import models
from django.conf import settings
from django.utils import timezone

class Name(models.Model):
    name = models.TextField()

class Form_of_delivery(models.Model):
    Form = models.TextField()


class Quantity(models.Model):
    quantity_hours = models.IntegerField()

def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title
