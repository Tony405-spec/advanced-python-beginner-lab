"""Mocking: unittest.mock, MagicMock, patch, and side_effect.

Run:
    pytest python/24_testing/examples/02_mocking.py -v
"""

from unittest.mock import MagicMock, Mock, call, patch

import pytest


# ---------------------------------------------------------------
# Code under test: something that talks to the outside world
# ---------------------------------------------------------------

def fetch_user(user_id: int, client) -> dict:
    """Fetch a user via a client object (which we'll mock in tests)."""
    response = client.get(f"/users/{user_id}")
    if response.status_code != 200:
        raise ValueError(f"failed to fetch user {user_id}: {response.status_code}")
    return response.json()


def send_welcome_email(user: dict, mailer) -> str:
    """Send a welcome email; return the mailer's message id."""
    return mailer.send(
        to=user["email"],
        subject="Welcome",
        body=f"Hello {user['name']}",
    )


# ---------------------------------------------------------------
# Mock basics
# ---------------------------------------------------------------

def test_mock_returns_mock_by_default():
    m = Mock()
    result = m.anything()
    assert isinstance(result, Mock)


def test_mock_with_return_value():
    m = Mock(return_value=42)
    assert m() == 42
    assert m() == 42  # always returns 42


def test_mock_records_calls():
    m = Mock()
    m(1, 2, key="value")
    m("hello")

    assert m.call_count == 2
    assert m.call_args_list == [
        call(1, 2, key="value"),
        call("hello"),
    ]


# ---------------------------------------------------------------
# Mock a client
# ---------------------------------------------------------------

def test_fetch_user_success():
    client = MagicMock()
    client.get.return_value.status_code = 200
    client.get.return_value.json.return_value = {"id": 1, "name": "Ada"}

    result = fetch_user(1, client)

    assert result == {"id": 1, "name": "Ada"}
    client.get.assert_called_once_with("/users/1")


def test_fetch_user_failure():
    client = MagicMock()
    client.get.return_value.status_code = 404

    with pytest.raises(ValueError, match="failed to fetch user 1: 404"):
        fetch_user(1, client)
