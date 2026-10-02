import pytest

from morse36 import (
    MalformedPacketError,
    PacketTooLargeError,
    UnknownCodeError,
    UnknownEntryError,
    decode,
    encode,
    verify_idempotency_key,
)


def test_round_trip_returns_semantic_entry(registry):
    raw = encode(registry, "example.publish", "order-123", "Linked In / News")

    assert raw.startswith("M36AXP1")
    assert len(raw) <= 36
    packet = decode(registry, raw)
    assert packet.entry.name == "example.publish"
    assert packet.entry.semantic["intent"] == "publish"
    assert packet.arg == "LINKEDINNEWS"
    assert packet.raw == raw


@pytest.mark.parametrize(
    "packet",
    [
        "",
        "M36AXP1",
        "M36BXP112345678",
        "M36AXP1nothex!!",
        "M36AXP112345678BAD ARG",
    ],
)
def test_malformed_packets_fail_explicitly(registry, packet):
    with pytest.raises(MalformedPacketError):
        decode(registry, packet)


def test_unknown_entry_and_code_fail_explicitly(registry):
    with pytest.raises(UnknownEntryError, match="missing"):
        encode(registry, "missing", "key")

    with pytest.raises(UnknownCodeError, match="ZZZ"):
        decode(registry, "M36AZZZ12345678")


def test_oversize_packet_fails_instead_of_truncating(registry):
    with pytest.raises(PacketTooLargeError, match="exceeds maximum 36"):
        encode(registry, "example.publish", "key", "X" * 22)


def test_full_idempotency_key_verifies_trace(registry):
    packet = decode(registry, encode(registry, "example.hold", "full-key-001"))

    assert verify_idempotency_key(packet, "full-key-001")
    assert verify_idempotency_key(packet.trace, "full-key-001")
    assert not verify_idempotency_key(packet, "full-key-002")
