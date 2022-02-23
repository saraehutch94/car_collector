from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='index'),
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('trees/', views.TreeList.as_view(), name='trees_index'),
    path('trees/<int:pk>/', views.TreeDetail.as_view(), name='trees_detail'),
    path('trees/create/', views.TreeCreate.as_view(), name='trees_create'),
    path('trees/<int:pk>/update/', views.TreeUpdate.as_view(), name='trees_update'),
]