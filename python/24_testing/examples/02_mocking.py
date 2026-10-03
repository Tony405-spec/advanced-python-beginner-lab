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
# ---------------------------------------------------------------
# side_effect: make a mock do more than return a value
# ---------------------------------------------------------------

def test_side_effect_sequence():
    m = Mock(side_effect=[1, 2, 3])
    assert m() == 1
    assert m() == 2
    assert m() == 3
    with pytest.raises(StopIteration):
        m()


def test_side_effect_exception():
    m = Mock(side_effect=ValueError("boom"))
    with pytest.raises(ValueError, match="boom"):
        m()


def test_side_effect_function():
    def double(x):
        return x * 2

    m = Mock(side_effect=double)
    assert m(5) == 10
    assert m(7) == 14


# ---------------------------------------------------------------
# Testing send_welcome_email with a mock mailer
# ---------------------------------------------------------------

def test_send_welcome_email_calls_mailer_with_correct_args():
    mailer = MagicMock()
    mailer.send.return_value = "msg-42"

    user = {"name": "Ada", "email": "ada@example.com"}
    result = send_welcome_email(user, mailer)

    assert result == "msg-42"
    mailer.send.assert_called_once_with(
        to="ada@example.com",
        subject="Welcome",
        body="Hello Ada",
    )


# ---------------------------------------------------------------
# patch: replace an object temporarily, automatically restore
# ---------------------------------------------------------------

def test_patch_replaces_function_temporarily():
    import os

    with patch("os.getcwd", return_value="/fake/path"):
        assert os.getcwd() == "/fake/path"

    # After the with block, os.getcwd is restored
    assert os.getcwd() != "/fake/path"


# ---------------------------------------------------------------
# autospec: mocks that respect the real signature
# ---------------------------------------------------------------

def test_magicmock_assert_not_called():
    mailer = MagicMock()
    assert mailer.send.call_count == 0
    mailer.send.assert_not_called()
