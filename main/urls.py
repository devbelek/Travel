from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TourViewSet, TourLocationViewSet, CommentListCreateView, CommentDetailView

router = DefaultRouter()
router.register(r'locations', TourLocationViewSet)
router.register(r'tours', TourViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),

]
