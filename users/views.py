from allauth.account.views import SignupView
from allauth.account.forms import SignupForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .models import GuideApplication, UserProfile
from .serializers import GuideApplicationSerializer, UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.middleware.csrf import get_token
import logging

logger = logging.getLogger(__name__)

User = get_user_model()


def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})


@method_decorator(csrf_protect, name='dispatch')
class CustomSignupView(APIView):
    def post(self, request):
        form = SignupForm(request.data)
        if form.is_valid():
            user = form.save(request)
            return Response({'detail': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


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
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        else:
            print("Validation error:", serializer.errors)
