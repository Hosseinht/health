import pytest
from django.contrib.auth import get_user_model
from rest_framework import status

from glucose.models import UserProfile

User = get_user_model()


@pytest.mark.django_db()
class TestGlucose:
    def test_create_glucose_return_201(self, api_client, glucose_factory, create_user):
        user = create_user
        userprofile = UserProfile.objects.get(user=user)
        glucose = glucose_factory.create(user=userprofile)
        response = api_client.post(
            "/api/v1/levels/",
            {
                "user": glucose.user.pk,
                "gerät": glucose.gerät,
                "seriennummer": glucose.seriennummer,
                "aufzeichnungstyp": glucose.aufzeichnungstyp,
                "glukosewert": glucose.glukosewert,
                "gerätezeitstempel": glucose.gerätezeitstempel,
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["id"] > 0

    def test_get_glucose_return_200(self, api_client):
        response = api_client.get("/api/v1/levels/")

        assert response.status_code == status.HTTP_200_OK

    def test_if_glucose_exist_return_200(
            self, api_client, glucose_factory, create_user
    ):
        user = create_user
        userprofile = UserProfile.objects.get(user=user)
        glucose = glucose_factory.create(user=userprofile)

        response = api_client.get(f"/api/v1/levels/{glucose.id}/")

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            "id": glucose.id,
            "user": glucose.user.pk,
            "gerät": glucose.gerät,
            "seriennummer": glucose.seriennummer,
            "aufzeichnungstyp": glucose.aufzeichnungstyp,
            "glukosewert": glucose.glukosewert,
            "gerätezeitstempel": glucose.gerätezeitstempel,
        }
