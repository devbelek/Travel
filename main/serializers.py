from rest_framework import serializers
from .models import Tour, TourLocation, Comment, TourDescription, TourItinerary, PlaceToLive
from users.serializers import GuidesSerializer


class TourDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourDescription
        fields = '__all__'


class TourStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourDescription
        fields = '__all__'


class TourLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourLocation
        fields = '__all__'


class TourItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = TourItinerary
        fields = '__all__'


class PlaceToLiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceToLive
        fields = '__all__'


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
    location = TourLocationSerializer()
    guide = GuidesSerializer()
    description = TourDescriptionSerializer()
    itinerary = TourItinerarySerializer()
    place_to_live = PlaceToLiveSerializer()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Tour
        fields = '__all__'