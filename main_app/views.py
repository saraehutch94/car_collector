from ast import Pass
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car, Tree
from .forms import GasForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

@login_required
def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    trees_car_doesnt_have = Tree.objects.exclude(id__in = car.trees.all().values_list('id'))
    gas_form = GasForm()
    return render(request, 'cars/detail.html', {
        'car': car,
        'gas_form': gas_form,
        'trees': trees_car_doesnt_have
    })

@login_required
def assoc_tree(request, car_id, tree_id):
    Car.objects.get(id=car_id).trees.add(tree_id)
    return redirect('detail', car_id=car_id)

@login_required
def delete_tree_from_car(request, car_id, tree_id):
    Car.objects.get(id=car_id).trees.remove(tree_id)
    return redirect('detail', car_id=car_id)

@login_required
def add_gas(request, car_id):
    form = GasForm(request.POST)
    if form.is_valid():
        new_gas = form.save(commit=False)
        new_gas.car_id = car_id
        new_gas.save()
    return redirect('detail', car_id=car_id)

def signup(request):
    error_message = ''
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign-up credentials. Please try again.'
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form, 'error_message': error_message})

class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = ('make', 'model', 'color', 'description')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CarUpdate(LoginRequiredMixin, UpdateView):
    model = Car
    fields = '__all__'

class CarDelete(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = '/cars/'

class TreeList(LoginRequiredMixin, ListView):
    model = Tree

class TreeDetail(LoginRequiredMixin, DetailView):
    model = Tree

class TreeCreate(LoginRequiredMixin, CreateView):
    model = Tree
    fields = '__all__'

class TreeUpdate(LoginRequiredMixin, UpdateView):
    model = Tree
    fields = '__all__'

class TreeDelete(LoginRequiredMixin, DeleteView):
    model = Tree
    success_url = '/trees/'