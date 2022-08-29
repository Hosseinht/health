from rest_framework import generics

from .models import Glucose
from .serializers import GlucoseSerializer


class GlucoseListView(generics.ListCreateAPIView):
    queryset = Glucose.objects.all()
    serializer_class = GlucoseSerializer


class GlucoseRetrieveView(generics.RetrieveAPIView):
    queryset = Glucose.objects.all()
    serializer_class = GlucoseSerializer
