from rest_framework import serializers
from .models import GuideApplication, Tour


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['title', 'description', 'price', 'guide']


class GuideApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuideApplication
        fields = ['name', 'surname', 'resume']
