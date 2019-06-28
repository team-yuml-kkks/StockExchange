import re

from faker import Faker
from hypothesis.strategies import composite
from rest_framework_jwt.settings import api_settings


def to_snake(name):
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2',
        re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    ).lower()


class TestFactory:
    """
    Provides mock objects for app-specific models.
    Tester should not worry about boilerplate state instantiation,
    if it's not the focus of the test. This class wraps around factory boy's
    Factories, in order to provide uniform interface for the tester, i.e.
    _all_ mock objects are created via this instance and nothing else.

    Additionally, `TestFactory` provides access to `Faker` functionality,
    effectively hiding this dependency.
    """
    factories = {}

    @classmethod
    def register(cls, factory_cls):
        name = factory_cls.__name__.replace('Factory', '')
        name = to_snake(name)
        cls.factories[name] = factory_cls

    def __init__(self):
        self.faker = Faker()

    def __getattr__(self, key):
        if key in self.factories.keys():
            return self.factories[key]

        if hasattr(self.faker, key):
            return getattr(self.faker, key)

        return super().__getattr__(key)

"""
Register model factories here.

To register new model factory you have to:

1. Import factory from module.
2. Register it to TestFactory with:
    `TestFactory.register(ModelFactory)`

Example:

from test.module import ModelFactory
TestFactory.register(ModelFactory)
"""

from stock_exchange.apps.users.factory import UserFactory

TestFactory.register(UserFactory)

factory = TestFactory()

# This is needed to test endpoints with JWT authorization.
def create_token_for_user(user):
    """Creates token for user to authenticate."""
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    return jwt_encode_handler(jwt_payload_handler(user))


@composite
def user_strategy(draw):
    """Creates user with JWT token."""
    user = factory.user(password=Faker().isbn10())

    return (user, create_token_for_user(user))
