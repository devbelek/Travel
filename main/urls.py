from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AboutViewSet, TourViewSet

router = DefaultRouter()
router.register(r'about', AboutViewSet)
router.register(r'tours', TourViewSet)

urlpatterns = [
    path('', include(router.urls)),
]