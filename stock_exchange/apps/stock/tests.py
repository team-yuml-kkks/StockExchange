import pytest

from stock_exchange.apps.common.factory import TestFactory


factory = TestFactory()
pytestmark = pytest.mark.django_db
