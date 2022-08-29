from rest_framework import serializers

from .models import Glucose


class GlucoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glucose
        fields = ['id', 'user', 'gerät', 'seriennummer', 'aufzeichnungstyp', 'glukosewert']
