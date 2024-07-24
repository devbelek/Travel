from rest_framework import generics, viewsets
from .models import GuideApplication, UserProfile
from .serializers import GuideApplicationSerializer, UserProfileSerializer
from rest_framework.permissions import IsAuthenticated


class UserProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.userprofile


class GuideApplicationViewSet(viewsets.ModelViewSet):
    queryset = GuideApplication.objects.all()
    serializer_class = GuideApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
