from rest_framework import viewsets, generics, permissions
from .models import Tour, TourLocation, Comment, TourDescription, TourItinerary, PlaceToLive
from .serializers import TourSerializer, TourLocationSerializer, CommentSerializer, TourDescriptionSerializer, \
    TourItinerarySerializer, PlaceToLiveSerializer
from .permissions import IsAdminOrGuide, IsOwnerOrReadOnly
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [IsAdminOrGuide]

class TourLocationViewSet(viewsets.ModelViewSet):
    queryset = TourLocation.objects.all()
    serializer_class = TourLocationSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentDetailView(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class TourDescriptionViewSet(viewsets.ModelViewSet):
    queryset = TourDescription.objects.all()
    serializer_class = TourDescriptionSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class TourItineraryViewSet(viewsets.ModelViewSet):
    queryset = TourItinerary.objects.all()
    serializer_class = TourItinerarySerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class PlaceToLiveViewSet(viewsets.ModelViewSet):
    queryset = PlaceToLive.objects.all()
    serializer_class = PlaceToLiveSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
