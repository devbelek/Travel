from .models import Tour, About, TourLocation, Booking
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


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    tour = TourSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['tour', 'phone_num']

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)