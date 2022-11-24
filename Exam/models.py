from django.db import models
from django.conf import settings
from django.utils import timezone

class Name(models.Model):
    Name = models.TextField()

class Date_of_exam(models.Model):
    date = models.DateTimeField()

class Date_of_reexam(models.Model):
    date = models.DateTimeField()

def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title
