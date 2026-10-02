"""Installable, registry-driven Morse/36 wire library."""

from .codec import (
    DecodedPacket,
    decode,
    encode,
    sanitize_arg,
    trace_fingerprint,
    verify_idempotency_key,
)
from .errors import (
    DecodeError,
    EncodeError,
    MalformedPacketError,
    Morse36Error,
    PacketTooLargeError,
    RegistryDigestError,
    RegistryError,
    RegistrySchemaError,
    UnknownCodeError,
    UnknownEntryError,
)
from .registry import SCHEMA, Registry, RegistryEntry, canonical_digest

__all__ = [
    "SCHEMA",
    "DecodeError",
    "DecodedPacket",
    "EncodeError",
    "MalformedPacketError",
    "Morse36Error",
    "PacketTooLargeError",
    "Registry",
    "RegistryDigestError",
    "RegistryEntry",
    "RegistryError",
    "RegistrySchemaError",
    "UnknownCodeError",
    "UnknownEntryError",
    "canonical_digest",
    "decode",
    "encode",
    "sanitize_arg",
    "trace_fingerprint",
    "verify_idempotency_key",
]
