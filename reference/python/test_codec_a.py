from codec_a import decode, encode
from morse36 import Registry, canonical_digest


def test_round_trip():
    document = {
        "schema": "morse36.registry/v1",
        "profile": "reference",
        "header": "M36A",
        "max_packet": 36,
        "entries": [
            {
                "name": "example.signal",
                "code": "EX1",
                "semantic": {"intent": "example"},
            }
        ],
    }
    document["digest"] = canonical_digest(document)
    registry = Registry.from_dict(document)

    raw = encode(registry, "example.signal", "research-001", "DEMO")
    assert len(raw) <= 36
    packet = decode(registry, raw)
    assert packet.entry.semantic["intent"] == "example"
    assert packet.arg == "DEMO"
