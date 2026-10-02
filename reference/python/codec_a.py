"""Codec-A reference wrapper.

Applications supply an immutable compiled registry artifact; this module has no
David Labs or other domain-private word assignments.
"""

from morse36 import (
    DecodedPacket as Packet,
    Registry,
    decode as _decode,
    encode as _encode,
    verify_idempotency_key,
)


def load_registry(path: str) -> Registry:
    return Registry.load(path)


def encode(
    registry: Registry, entry_name: str, trace_id: str, arg: str = ""
) -> str:
    return _encode(registry, entry_name, trace_id, arg)


def decode(registry: Registry, packet: str) -> Packet:
    return _decode(registry, packet)
