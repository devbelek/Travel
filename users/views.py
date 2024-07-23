from rest_framework import generics, viewsets
from .models import Tour, GuideApplication
from .serializers import TourSerializer, GuideApplicationSerializer
from .permissions import IsGuide


class TourCreateView(generics.CreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [IsGuide]


class GuideApplicationViewSet(viewsets.ModelViewSet):
    queryset = GuideApplication.objects.all()
    serializer_class = GuideApplicationSerializer
