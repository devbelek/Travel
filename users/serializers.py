from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserProfile, GuideApplication, Guides

User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class GuideApplicationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    user_profile = UserProfileSerializer(source='user.userprofile', read_only=True)

    class Meta:
        model = GuideApplication
        fields = ['id', 'user', 'user_profile', 'name', 'surname', 'resume', 'is_approved']


class GuidesSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Guides
        fields = ['id', 'full_name']

    def get_full_name(self, obj):
        return f"{obj.guideapplication.name} {obj.guideapplication.surname}"
