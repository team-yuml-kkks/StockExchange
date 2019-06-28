import factory
from factory import LazyFunction
from factory.django import DjangoModelFactory as Factory
from faker import Faker

from .models import User


class UserFactory(Factory):
    class Meta:
        model = User

    email = factory.Faker('email')
    username = factory.Faker('pystr')

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

    account_number = factory.Faker('credit_card_number')
    bank_name = factory.Faker('company')
    address = factory.Faker('street_address')
    city_code = factory.Faker('zipcode')
