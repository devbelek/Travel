from .models import Tour
from rest_framework import serializers


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['title', 'description', 'price', 'guide']
