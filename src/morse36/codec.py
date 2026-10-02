"""Registry-driven Codec-A wire operations."""
from __future__ import annotations

import hashlib
import hmac
import re
from dataclasses import dataclass

from .errors import (
    MalformedPacketError,
    PacketTooLargeError,
    UnknownCodeError,
    UnknownEntryError,
)
from .registry import Registry, RegistryEntry

_ARG_STRIP_RE = re.compile(r"[^A-Z0-9._:-]+")
_SAFE_ARG_RE = re.compile(r"^[A-Z0-9._:-]*$")
_TRACE_RE = re.compile(r"^[0-9A-F]{8}$")


@dataclass(frozen=True)
class DecodedPacket:
    """A decoded packet and the registry semantics to which it resolves."""

    entry: RegistryEntry
    trace: str
    arg: str
    raw: str


def trace_fingerprint(idempotency_key: str) -> str:
    """Create the eight-character wire fingerprint for a full trace key."""
    if not isinstance(idempotency_key, str) or not idempotency_key:
        raise ValueError("idempotency_key must be a non-empty string")
    return hashlib.blake2s(
        idempotency_key.encode("utf-8"), digest_size=4
    ).hexdigest().upper()


def sanitize_arg(arg: str) -> str:
    """Uppercase an optional argument and remove non-wire characters."""
    if not isinstance(arg, str):
        raise TypeError("arg must be a string")
    return _ARG_STRIP_RE.sub("", arg.upper())


def encode(
    registry: Registry,
    entry_name: str,
    idempotency_key: str,
    arg: str = "",
) -> str:
    """Encode a named registry entry as a bounded Morse/36 packet."""
    entry = registry.entry_for_name(entry_name)
    if entry is None:
        raise UnknownEntryError(f"unknown registry entry: {entry_name}")
    packet = (
        registry.header
        + entry.code
        + trace_fingerprint(idempotency_key)
        + sanitize_arg(arg)
    )
    if len(packet) > registry.max_packet:
        raise PacketTooLargeError(
            f"packet length {len(packet)} exceeds maximum {registry.max_packet}"
        )
    return packet


def decode(registry: Registry, packet: str) -> DecodedPacket:
    """Decode a packet using exactly one immutable registry."""
    if not isinstance(packet, str):
        raise MalformedPacketError("packet must be a string")
    minimum = len(registry.header) + 3 + 8
    if not minimum <= len(packet) <= registry.max_packet:
        raise MalformedPacketError(
            f"packet length must be between {minimum} and {registry.max_packet}"
        )
    if not packet.startswith(registry.header):
        raise MalformedPacketError(
            f"packet header does not match profile {registry.profile!r}"
        )
    code_start = len(registry.header)
    code = packet[code_start : code_start + 3]
    trace = packet[code_start + 3 : code_start + 11]
    arg = packet[code_start + 11 :]
    if not _TRACE_RE.fullmatch(trace):
        raise MalformedPacketError("packet trace must be eight uppercase hex characters")
    if not _SAFE_ARG_RE.fullmatch(arg):
        raise MalformedPacketError("packet argument contains non-canonical characters")
    entry = registry.entry_for_code(code)
    if entry is None:
        raise UnknownCodeError(f"unknown registry code: {code}")
    return DecodedPacket(entry=entry, trace=trace, arg=arg, raw=packet)


def verify_idempotency_key(
    packet_or_trace: DecodedPacket | str, idempotency_key: str
) -> bool:
    """Verify a full idempotency key against a packet's trace fingerprint."""
    trace = (
        packet_or_trace.trace
        if isinstance(packet_or_trace, DecodedPacket)
        else packet_or_trace
    )
    if not isinstance(trace, str) or not _TRACE_RE.fullmatch(trace):
        raise ValueError("trace must be eight uppercase hex characters")
    return hmac.compare_digest(trace, trace_fingerprint(idempotency_key))
