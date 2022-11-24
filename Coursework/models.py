from django.db import models
from django.conf import settings
from django.utils import timezone


class Name_cours(models.Model):
    Name = models.TextField()

class Student(models.Model):
    Second_name = models.TextField()
    First_name = models.TextField()
    Middle_name = models.TextField()

class Scientific_leader(models.Model):
    Second_name = models.TextField()
    First_name = models.TextField()
    Middle_name = models.TextField()

class Field(models.Model):
    Field = models.TextField()


def publish(self):
    self.published_date = timezone.now()
    self.save()


def __str__(self):
    return self.title
