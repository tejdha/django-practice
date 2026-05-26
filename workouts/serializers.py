from rest_framework import serializers
from .models import workouts

class Workoutserializer(serializers.ModelSerializer):

    class Meta:
        model = workouts
        fields = '__all__'

    