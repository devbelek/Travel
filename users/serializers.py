from rest_framework import serializers
from .models import GuideApplication

class GuideApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuideApplication
        fields = ['name', 'surname', 'resume']
