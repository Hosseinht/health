import factory.fuzzy
from faker import Faker
from django.contrib.auth import get_user_model

from glucose.models import Glucose, UserProfile

fake = Faker()

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "john%s" % n)


class UserProfileFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)


class GlucoseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Glucose

    user = factory.SubFactory(UserProfileFactory)
    gerät = fake.text(max_nb_chars=5)
    seriennummer = fake.sentence(nb_words=5)
    aufzeichnungstyp = fake.random_int(min=0, max=4)
    glukosewert = fake.random_int(min=0, max=4)
    gerätezeitstempel = "2021-09-04T22:14:18Z"
