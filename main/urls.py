from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TourViewSet, TourLocationViewSet, CommentListCreateView, CommentDetailView, TourDescriptionViewSet, \
    TourItineraryViewSet, PlaceToLiveViewSet, TourStepViewSet

router = DefaultRouter()
router.register(r'steps', TourStepViewSet, basename='tour-step')
router.register(r'tours', TourViewSet, basename='tour')
router.register(r'descriptions', TourDescriptionViewSet, basename='tour-description')
router.register(r'itineraries', TourItineraryViewSet, basename='tour-itinerary')
router.register(r'places_to_live', PlaceToLiveViewSet, basename='place-to-live')
router.register(r'location', TourLocationViewSet, basename='tour-location')

urlpatterns = [
    path('', include(router.urls)),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
