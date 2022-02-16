from django.shortcuts import render

'''
This is our fake database (changing later):
'''

class Car:
    def __init__(self, make, model, color, description):
        self.make = make
        self.model = model
        self.color = color
        self.description = description

# list of cars
cars = [
    Car('Tesla', 'Model X', 'blue', 'my future car that will be named blueberry'),
    Car('Kia', 'EV6', 'silver', 'wowee'),
    Car('Kia', 'Stinger', 'Ascot Green', 'fast car'),
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    return render(request, 'cars/index.html', {'cars': cars})