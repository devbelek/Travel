from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GuideApplicationViewSet, TourCreateView

router = DefaultRouter()
router.register(r'guide_registration', GuideApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tours/', TourCreateView.as_view(), name='tour-create'),
]
