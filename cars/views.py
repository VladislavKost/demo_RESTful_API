from django.shortcuts import render
from rest_framework import generics
from cars.serializers import CarDetailSerializer, CarsListSerializer
from cars.models import Car
from cars.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.


class CarCreateView(generics.CreateAPIView): #создание записей в БД
    serializer_class = CarDetailSerializer


class CarsListView(generics.ListAPIView): #Вывод всей информации из БД
    serializer_class = CarsListSerializer
    queryset = Car.objects.all()
    # permission_classes = (IsAuthenticated, ) #разрешение на просмотр записей. Неавторизованный пользователь ничего не увидит
    permission_classes = (IsAdminUser,) #просмотр записей только у Админа

class CarDetailView(generics.RetrieveUpdateDestroyAPIView): #редактирование объекта и удаление
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly, ) #разрешение на редактирование

