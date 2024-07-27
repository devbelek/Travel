from rest_framework import serializers
from .models import Tour, TourLocation, Comment

class TourLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourLocation
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = '__all__'

class TourSerializer(serializers.ModelSerializer):
    location = serializers.PrimaryKeyRelatedField(queryset=TourLocation.objects.all())
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Tour
        fields = '__all__'
