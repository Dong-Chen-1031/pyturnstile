"""Client class for Cloudflare Turnstile token validation, providing both sync and async methods."""

from __future__ import annotations

from typing import Optional

from . import core


class Turnstile:
    """
    A client for validating Cloudflare Turnstile tokens.

    This class provides both synchronous and asynchronous methods to validate
    Turnstile tokens with Cloudflare's verification API.

    Attributes:
        secret: Your Cloudflare Turnstile secret key

    Example:
        Synchronous usage:
        >>> turnstile = Turnstile(secret="your-secret-key")
        >>> response = turnstile.validate(token="user-token")
        >>> if response.success:
        ...     print("Valid token")

        Asynchronous usage:
        >>> turnstile = Turnstile(secret="your-secret-key")
        >>> response = await turnstile.async_validate(token="user-token")
        >>> if response.success:
        ...     print("Valid token")
    """

    def __init__(self, secret: str):
        self.secret = secret

    def validate(
        self,
        token: str,
        remoteip: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: int = 10,
    ) -> core.TurnstileResponse:
        """
        Validate a Turnstile token with Cloudflare's API.
        Args:
            token: The token from the client-side widget
            remoteip: (Optional) The visitor's IP address
            idempotency_key: (Optional) UUID for retry protection
            timeout: (Optional) Timeout for the API request in seconds
        Returns:
            TurnstileResponse: The response from the Turnstile API
        Raises:
            TurnstileValidationError: If the validation fails due to an API error or network issue
        """
        return core.validate(token, self.secret, remoteip, idempotency_key, timeout)

    async def async_validate(
        self,
        token: str,
        remoteip: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: int = 10,
    ) -> core.TurnstileResponse:
        """
        Asynchronously validate a Turnstile token with Cloudflare's API.
        Args:
            token: The token from the client-side widget
            remoteip: (Optional) The visitor's IP address
            idempotency_key: (Optional) UUID for retry protection
            timeout: (Optional) Timeout for the API request in seconds
        Returns:
            TurnstileResponse: The response from the Turnstile API
        Raises:
            TurnstileValidationError: If the validation fails due to an API error or network issue
        """
        return await core.async_validate(
            token, self.secret, remoteip, idempotency_key, timeout
        )


__all__ = ["Turnstile"]
