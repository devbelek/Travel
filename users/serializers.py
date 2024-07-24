from rest_framework import serializers
from .models import GuideApplication, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'date_of_birth', 'gender', 'phone_number', 'country', 'city', 'address', 'postal_code']


class GuideApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuideApplication
        fields = ['name', 'surname', 'resume']
