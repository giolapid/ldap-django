from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Person(models.Model):
    input = models.CharField(max_length=200)
    result = models.TextField()

    def __str__(self):
        return self.name