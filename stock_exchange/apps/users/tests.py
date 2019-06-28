import pytest

from .models import User

from stock_exchange.apps.common.factory import TestFactory


factory = TestFactory()
pytestmark = pytest.mark.django_db


def test_user_factory():
    user = factory.user()

    assert user
    assert isinstance(user, User)


def test_user_factory_username():
    user = factory.user(username="Test")
   
    assert user
    assert user.username == "Test"
