import pytest

from api_client import get_user


def test_get_user():
    response = get_user(1)
    assert response.status_code == 200

def test_get_nonexistent_user():
    response = get_user(999)
    assert response.status_code == 404

