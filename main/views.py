from rest_framework import generics
from .models import Tour
from .serializers import TourSerializer
from .permissions import IsGuide


class TourCreateView(generics.CreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [IsGuide]
