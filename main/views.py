from rest_framework import generics, viewsets
from .models import Tour, About, TourLocation
from .serializers import TourSerializer, AboutSerializer, TourLocationSerializer
from .permissions import IsAdminOrGuide
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly


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
