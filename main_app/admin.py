from django.contrib import admin
from .models import Car, Tree, Gas, Photo

# Register your models here.
admin.site.register(Car)
admin.site.register(Tree)
admin.site.register(Gas)
admin.site.register(Photo)