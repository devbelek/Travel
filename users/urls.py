from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GuideApplicationViewSet

router = DefaultRouter()
router.register(r'guide_registration', GuideApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
