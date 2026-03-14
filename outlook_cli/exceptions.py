"""Structured exception hierarchy for outlook-cli."""

from __future__ import annotations


class OutlookCliError(Exception):
    """Base exception for all outlook-cli errors."""


class TokenExpiredError(OutlookCliError):
    """401 — bearer token expired or revoked."""


class RateLimitError(OutlookCliError):
    """429 — API rate limit hit after max retries."""


class ResourceNotFoundError(OutlookCliError):
    """Folder, calendar, category, signature, or message not found."""


class AuthRequiredError(OutlookCliError):
    """No token available — user must run 'outlook login'."""
