from rest_framework import serializers

from .models import Glucose, UserProfile


class GlucoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glucose
        fields = ["glukosewert", "gerätezeitstempel", ]


class GlucosePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glucose
        fields = [
            "id",
            "user",
            "gerät",
            "seriennummer",
            "aufzeichnungstyp",
            "glukosewert",
            "gerätezeitstempel",
        ]


class GlucoseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glucose
        fields = [
            "id",
            "user",
            "gerät",
            "seriennummer",
            "aufzeichnungstyp",
            "glukosewert",
            "gerätezeitstempel"
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    glucose = serializers.SerializerMethodField()
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    def get_glucose(self, obj):
        # limit number of glucose level to 2
        glucose = obj.glucose.all()[0:2]
        return GlucoseSerializer(glucose, many=True).data

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'glucose']
