from rest_framework import generics, viewsets
from .models import Tour, About, TourLocation, Booking
from .serializers import TourSerializer, AboutSerializer, TourLocationSerializer, BookingCreateSerializer, \
    BookingSerializer
from .permissions import IsAdminOrGuide
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [IsAdminOrGuide]


class TourLocationViewSet(viewsets.ModelViewSet):
    queryset = TourLocation.objects.all()
    serializer_class = TourLocationSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return BookingCreateSerializer
        return BookingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(user=self.request.user)
