from codec_a import decode, encode


def test_round_trip():
    raw = encode("PUBLISH", "research-001", "LINKEDIN")
    assert len(raw) <= 36
    packet = decode(raw)
    assert packet.intent == "PUBLISH"
    assert packet.arg == "LINKEDIN"
