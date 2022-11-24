from django.db import models
from django.conf import settings
from django.utils import timezone

class Name(models.Model):
    Second_name = models.TextField()
    First_name = models.TextField()
    Middle_name = models.TextField()

class Number_of_student(models.Model):
    number = models.IntegerField()

class Place_of_work(models.Model):
    text = models.TextField()

class Year_of_born(models.Model):
    date = models.DateTimeField()

class Address(models.Model):
    address = models.TextField()

class Title_of_diplome(models.Model):
    title = models.TextField()

def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title
