from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GuideApplicationViewSet, UserProfileDetail, get_csrf_token, CustomSignupView

router = DefaultRouter()
router.register(r'new_guide', GuideApplicationViewSet)

urlpatterns = [
    path('csrf_token/', get_csrf_token, name='csrf_token'),
    path('', include(router.urls)),
    path('profile/', UserProfileDetail.as_view(), name='user-profile'),
    path('signup/', CustomSignupView.as_view(), name='rest_signup'),
]
