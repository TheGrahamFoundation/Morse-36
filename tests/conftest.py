import json

import pytest

from morse36 import Registry, canonical_digest


@pytest.fixture
def registry_document():
    document = {
        "schema": "morse36.registry/v1",
        "profile": "test-codec-a",
        "header": "M36A",
        "max_packet": 36,
        "entries": [
            {
                "name": "example.publish",
                "code": "XP1",
                "semantic": {
                    "intent": "publish",
                    "mutation": True,
                    "arguments": ["channel"],
                },
            },
            {
                "name": "example.hold",
                "code": "XH1",
                "semantic": {"intent": "hold", "mutation": False},
            },
        ],
    }
    document["digest"] = canonical_digest(document)
    return document


@pytest.fixture
def registry_path(tmp_path, registry_document):
    path = tmp_path / "registry.json"
    path.write_text(json.dumps(registry_document), encoding="utf-8")
    return path


@pytest.fixture
def registry(registry_path):
    return Registry.load(registry_path)
