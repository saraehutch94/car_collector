from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car, Tree
from .forms import GasForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    gas_form = GasForm()
    return render(request, 'cars/detail.html', {
        'car': car,
        'gas_form': gas_form
    })

class CarCreate(CreateView):
    model = Car
    fields = '__all__'

class CarUpdate(UpdateView):
    model = Car
    fields = '__all__'

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'

class TreeList(ListView):
    model = Tree

class TreeDetail(DetailView):
    model = Tree

class TreeCreate(CreateView):
    model = Tree
    fields = '__all__'

class TreeUpdate(UpdateView):
    model = Tree
    fields = '__all__'

class TreeDelete(DeleteView):
    model = Tree
    success_url = '/trees/'