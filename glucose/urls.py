from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .views import GlucoseListView, GlucoseRetrieveView, UserViewSet, GlucoseViewSet

router = DefaultRouter()

router.register('userprofile', UserViewSet)

userprofile_router = routers.NestedDefaultRouter(router, 'userprofile', lookup='userprofile')
userprofile_router.register('glucose', GlucoseViewSet, basename='glucose')

urlpatterns = [
    path('levels/', GlucoseListView.as_view()),
    path('levels/<int:pk>/', GlucoseRetrieveView.as_view()),

] + router.urls + userprofile_router.urls
