"""Live smoke tests for real Outlook access.

These are intentionally opt-in. Run them with:
  OUTLOOK_RUN_SMOKE=1 OUTLOOK_TOKEN=... pytest -m smoke
"""

from __future__ import annotations

import os

import pytest

from outlook_cli.auth import verify_token
from outlook_cli.client import OutlookClient

pytestmark = pytest.mark.smoke


def _require_live_token() -> str:
    if os.environ.get("OUTLOOK_RUN_SMOKE") != "1":
        pytest.skip("Set OUTLOOK_RUN_SMOKE=1 to enable live smoke tests.")
    token = os.environ.get("OUTLOOK_TOKEN")
    if not token:
        pytest.skip("Set OUTLOOK_TOKEN to run live smoke tests.")
    return token


def test_smoke_verify_token():
    token = _require_live_token()
    assert verify_token(token) is True


def test_smoke_whoami():
    token = _require_live_token()
    client = OutlookClient(token)
    me = client.get_me()

    assert me.get("DisplayName")
    assert me.get("EmailAddress")


def test_smoke_inbox_fetch():
    token = _require_live_token()
    client = OutlookClient(token)
    messages = client.get_messages(top=1)

    assert isinstance(messages, list)
