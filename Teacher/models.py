from django.db import models
from django.conf import settings
from django.utils import timezone

class Name(models.Model):
    Second_name = models.TextField()
    First_name = models.TextField()
    Middle_name = models.TextField()

class Email(models.Model):
    E_mail = models.EmailField()

class Academic_degree(models.Model):
    text = models.TextField()

class Rank(models.Model):
    text = models.TextField()

class Place_of_work(models.Model):
    text = models.TextField()

class Foto(models.Model):
    image = models.ImageField()

def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title