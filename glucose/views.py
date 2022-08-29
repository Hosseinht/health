from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from .filters import GlucoseFilter
from .models import Glucose, UserProfile
from .serializers import (GlucoseDetailSerializer, GlucosePostSerializer,
                          UserProfileSerializer)


class GlucoseListView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = GlucoseFilter

    def get_serializer_class(self):
        if self.request.method == "POST":
            return GlucosePostSerializer
        else:
            return UserProfileSerializer


class GlucoseRetrieveView(generics.RetrieveAPIView):
    queryset = Glucose.objects.all()
    serializer_class = GlucoseDetailSerializer
