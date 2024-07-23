from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AboutViewSet, TourViewSet, TourLocationViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'about', AboutViewSet)
router.register(r'locations', TourLocationViewSet)
router.register(r'tours', TourViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]