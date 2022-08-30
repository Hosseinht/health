from django_filters.rest_framework import FilterSet

from .models import Glucose


class GlucoseFilter(FilterSet):
    class Meta:
        model = Glucose
        fields = {
            'gerätezeitstempel': ['date__gte', 'date__lte'],
            'glukosewert': ['gte', 'lte'],
        }
