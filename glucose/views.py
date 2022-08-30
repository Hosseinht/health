from django_filters.rest_framework import DjangoFilterBackend
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import (BrowsableAPIRenderer, JSONRenderer)

from rest_framework.viewsets import ModelViewSet
from rest_framework_csv import renderers as r

from .filters import GlucoseFilter
from .models import Glucose, UserProfile
from .serializers import GlucoseDetailSerializer, UserProfileSerializer


class GlucoseListView(XLSXFileMixin, generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()

    filter_backends = [DjangoFilterBackend, OrderingFilter]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return GlucoseDetailSerializer
        else:
            return UserProfileSerializer


class MyCsvRenderer(r.CSVRenderer):
    header = [
        "id",
        "user",
        "gerät",
        "seriennummer",
        "aufzeichnungstyp",
        "glukosewert",
        "gerätezeitstempel",
    ]


class GlucoseRetrieveView(XLSXFileMixin, generics.RetrieveAPIView):
    queryset = Glucose.objects.all()
    serializer_class = GlucoseDetailSerializer


# ViewSet Views
class UserViewSet(ModelViewSet):
    """
        http://127.0.0.1:8000/api/v1/userprofile
        Display Users and their glucose level limited to 4 level

        http://127.0.0.1:8000/api/v1/userprofile/{id}/
        Display a single user and glucose level limited to 4 level
    """
    http_method_names = ['get', 'post']
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return GlucoseDetailSerializer
        else:
            return UserProfileSerializer


class GlucoseViewSet(XLSXFileMixin, ModelViewSet):
    """
        http://127.0.0.1:8000/api/v1/userprofile/{2}/glucose/
        list of glucose level for the given user

        http://127.0.0.1:8000/api/v1/userprofile/2/glucose/1/
        display a single glucose level
    """

    http_method_names = ['get', 'post']
    serializer_class = GlucoseDetailSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = GlucoseFilter
    ordering_fields = ["gerät", "glukosewert", "gerätezeitstempel"]

    renderer_classes = [BrowsableAPIRenderer, JSONRenderer, XLSXRenderer, MyCsvRenderer]

    def get_queryset(self):
        return Glucose.objects.filter(user_id=self.kwargs["userprofile_pk"]).order_by(
            "-gerätezeitstempel"
        )
