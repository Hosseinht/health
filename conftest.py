import pytest

from pytest_factoryboy import register
from rest_framework.test import APIClient

from glucose.tests.factories import GlucoseFactory, UserFactory, UserProfileFactory

register(GlucoseFactory)
register(UserFactory)
register(UserProfileFactory)


@pytest.fixture()
def api_client():
    return APIClient()


@pytest.fixture()
def create_user(db, user_factory):
    return user_factory.create()


@pytest.fixture()
def create_userprofile(db, user_profile_factory, create_user):
    return user_profile_factory.create(user=create_user)
