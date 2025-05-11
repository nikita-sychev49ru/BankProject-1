import pytest


@pytest.fixture
def not_valid_date():
    return '11 марта 2024'


@pytest.fixture
def valid_date():
    return '2024-03-11T02:26:18.671407'
