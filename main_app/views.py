from ast import Pass
from django.shortcuts import render, redirect
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
    trees_car_doesnt_have = Tree.objects.exclude(id__in = car.trees.all().values_list('id'))
    gas_form = GasForm()
    return render(request, 'cars/detail.html', {
        'car': car,
        'gas_form': gas_form,
        'trees': trees_car_doesnt_have
    })

def assoc_tree(request, car_id, tree_id):
    Car.objects.get(id=car_id).trees.add(tree_id)
    return redirect('detail', car_id=car_id)

def add_gas(request, car_id):
    form = GasForm(request.POST)
    if form.is_valid():
        new_gas = form.save(commit=False)
        new_gas.car_id = car_id
        new_gas.save()
    return redirect('detail', car_id=car_id)

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