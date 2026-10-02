from copy import deepcopy

import pytest

from morse36 import (
    Registry,
    RegistryDigestError,
    RegistrySchemaError,
    canonical_digest,
)


def test_registry_is_immutable(registry):
    with pytest.raises(TypeError):
        registry.entries[0].semantic["intent"] = "changed"


def test_content_tampering_causes_digest_mismatch(registry_document):
    tampered = deepcopy(registry_document)
    tampered["entries"][0]["semantic"]["intent"] = "delete"

    with pytest.raises(RegistryDigestError, match="digest mismatch"):
        Registry.from_dict(tampered)


def test_wrong_digest_is_rejected(registry_document):
    document = deepcopy(registry_document)
    document["digest"] = "sha256:" + ("0" * 64)

    with pytest.raises(RegistryDigestError, match="digest mismatch"):
        Registry.from_dict(document)


@pytest.mark.parametrize("bad_code", ["abc", "AB", "ABCD", "A_B"])
def test_code_must_be_three_uppercase_alphanumerics(
    registry_document, bad_code
):
    document = deepcopy(registry_document)
    document["entries"][0]["code"] = bad_code
    document["digest"] = canonical_digest(document)

    with pytest.raises(RegistrySchemaError, match="three uppercase"):
        Registry.from_dict(document)


def test_codes_must_be_unique(registry_document):
    document = deepcopy(registry_document)
    document["entries"][1]["code"] = document["entries"][0]["code"]
    document["digest"] = canonical_digest(document)

    with pytest.raises(RegistrySchemaError, match="duplicate entry code"):
        Registry.from_dict(document)


def test_header_profile_and_envelope_are_validated(registry_document):
    for field, value, message in [
        ("header", "codec-a", "header"),
        ("profile", "Codec A", "profile"),
        ("max_packet", 37, "max_packet"),
    ]:
        document = deepcopy(registry_document)
        document[field] = value
        document["digest"] = canonical_digest(document)
        with pytest.raises(RegistrySchemaError, match=message):
            Registry.from_dict(document)
