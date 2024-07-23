from rest_framework import generics, viewsets
from .models import Tour, GuideApplication
from .serializers import TourSerializer, GuideApplicationSerializer
from .permissions import IsGuide
from rest_framework.permissions import IsAuthenticated


class TourCreateView(generics.CreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [IsGuide]


class GuideApplicationViewSet(viewsets.ModelViewSet):
    queryset = GuideApplication.objects.all()
    serializer_class = GuideApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
