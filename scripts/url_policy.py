"""Shared outbound URL policy for repository automation."""

from __future__ import annotations

from ipaddress import ip_address
from typing import Callable, Iterable
from urllib.parse import urlparse
from urllib.request import Request, urlopen


def _normalized_hosts(hosts: Iterable[str]) -> set[str]:
    return {host.rstrip(".").casefold() for host in hosts if host.strip()}


def same_site_hosts(hostname: str) -> set[str]:
    """Allow a host and its conventional www/non-www spelling only."""

    hostname = hostname.rstrip(".").casefold()
    if hostname.startswith("www."):
        return {hostname, hostname[4:]}
    return {hostname, f"www.{hostname}"}


def validate_public_https_url(
    url: str,
    *,
    allowed_hosts: Iterable[str] | None = None,
    label: str = "URL",
) -> str:
    """Return the normalized host after enforcing the public HTTPS boundary."""

    parsed = urlparse(url)
    if parsed.scheme.casefold() != "https":
        raise ValueError(f"{label} must use HTTPS")
    if parsed.username is not None or parsed.password is not None:
        raise ValueError(f"{label} must not contain embedded credentials")
    hostname = (parsed.hostname or "").rstrip(".").casefold()
    if not hostname:
        raise ValueError(f"{label} must include a hostname")
    if hostname == "localhost" or hostname.endswith(".localhost"):
        raise ValueError(f"{label} must use a public hostname")
    try:
        address = ip_address(hostname)
    except ValueError:
        address = None
    if address is not None and not address.is_global:
        raise ValueError(f"{label} must not use a non-public IP address")
    try:
        port = parsed.port
    except ValueError as exc:
        raise ValueError(f"{label} has an invalid port") from exc
    if port not in {None, 443}:
        raise ValueError(f"{label} must use the default HTTPS port")
    if allowed_hosts is not None and hostname not in _normalized_hosts(allowed_hosts):
        raise ValueError(f"{label} host is not approved: {hostname}")
    return hostname


def open_public_https(
    request: Request | str,
    *,
    timeout: float,
    opener: Callable[..., object] = urlopen,
    allowed_redirect_hosts: Iterable[str] | None = None,
) -> object:
    """Open a validated public HTTPS URL and validate the resulting redirect."""

    request_url = request.full_url if isinstance(request, Request) else request
    validate_public_https_url(request_url, label="Outbound URL")
    # The explicit policy check immediately above constrains urllib to public HTTPS.
    response = opener(request, timeout=timeout)  # nosec B310
    try:
        final_url = str(response.geturl())
        validate_public_https_url(
            final_url,
            allowed_hosts=allowed_redirect_hosts,
            label="Redirect URL",
        )
    except Exception:
        close = getattr(response, "close", None)
        if callable(close):
            close()
        raise
    return response
