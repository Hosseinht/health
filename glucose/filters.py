from django_filters.rest_framework import FilterSet

from .models import Glucose, UserProfile


class GlucoseFilter(FilterSet):
    class Meta:
        model = UserProfile
        fields = {
            'glucose__gerätezeitstempel': ['date__gte', 'date__lte']
        }
