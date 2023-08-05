from rest_framework import serializers
from cars.models import Car


class CarsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'vin', 'user')


class CarDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) #вставляется имя авторизованного пользователя из request

    class Meta:
        model = Car
        fields = '__all__'


