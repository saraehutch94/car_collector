from django.db import models
from django.urls import reverse

# Create your models here.

FILLS = (
    ('1', 'Week 1'),
    ('2', 'Week 2'),
    ('3', 'Week 3'),
    ('4', 'Week 4'),
)

class Tree(models.Model):
    scent = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.scent

    def get_absolute_url(self):
        return reverse('trees_detail', kwargs={'pk': self.id})

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    trees = models.ManyToManyField(Tree)

    def __str__(self):
        return (f'{self.make} {self.model}')

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

class Gas(models.Model):
    date = models.DateField('fill date')
    fill = models.CharField(max_length=1, choices=FILLS, default=FILLS[0][0])
    car = models.ForeignKey(Car, on_delete=models.CASCADE) 

    def __str__(self):
        return f'{self.get_fill_display()} on {self.date}'

    class Meta:
        ordering = ('date',)