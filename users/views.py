from rest_framework import generics, viewsets
from .models import GuideApplication
from .serializers import GuideApplicationSerializer
from rest_framework.permissions import IsAuthenticated


class GuideApplicationViewSet(viewsets.ModelViewSet):
    queryset = GuideApplication.objects.all()
    serializer_class = GuideApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
