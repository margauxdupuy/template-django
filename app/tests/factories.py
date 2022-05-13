import factory
from factory.django import DjangoModelFactory


class CallFactory(DjangoModelFactory):
    class Meta:
        model = Call

    type = factory.Faker("text", max_nb_chars=20)
    sid = factory.Faker("text", max_nb_chars=100)
