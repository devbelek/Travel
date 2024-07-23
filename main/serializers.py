from .models import Tour, About, TourLocation
from rest_framework import serializers


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        exclude = ['id']


class TourLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourLocation
        exclude = ['id']


class TourSerializer(serializers.ModelSerializer):
    location = serializers.PrimaryKeyRelatedField(queryset=TourLocation.objects.all())
    class Meta:
        model = Tour
        fields = '__all__'