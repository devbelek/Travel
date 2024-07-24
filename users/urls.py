from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GuideApplicationViewSet, UserProfileDetail

router = DefaultRouter()
router.register(r'new_guide', GuideApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', UserProfileDetail.as_view(), name='user-profile'),
]
