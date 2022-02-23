from django.db import models
from django.urls import reverse

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=30)
    description = models.TextField(max_length=250)

    def __str__(self):
        return (f'{self.make} {self.model}')

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

class Tree(models.Model):
    scent = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.scent

    def get_absolute_url(self):
        return reverse('trees_detail', kwargs={'pk': self.id})