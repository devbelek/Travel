from rest_framework import serializers
from .models import Tour, TourLocation, Comment, TourDescription
from users.serializers import GuidesSerializer


class TourDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourDescription
        fields = '__all__'


class TourLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourLocation
        fields = ['id', 'name', 'image', 'content']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):
    location = TourLocationSerializer()
    guide = GuidesSerializer()
    description = TourDescriptionSerializer()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Tour
        fields = '__all__'