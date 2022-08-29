from django.urls import path

from .views import GlucoseListView, GlucoseRetrieveView

urlpatterns = [
    path('levels/', GlucoseListView.as_view()),
    path('levels/<int:pk>/', GlucoseRetrieveView.as_view())
]
