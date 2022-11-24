from django.db import models
from django.conf import settings
from django.utils import timezone

class Mark(models.Model):
    Mark = models.IntegerField()


def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title