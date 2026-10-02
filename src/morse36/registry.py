"""Immutable, digest-bound Morse/36 registries."""
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from .errors import RegistryDigestError, RegistrySchemaError

SCHEMA = "morse36.registry/v1"
_CODE_RE = re.compile(r"^[A-Z0-9]{3}$")
_HEADER_RE = re.compile(r"^M36[A-Z0-9]+$")
_NAME_RE = re.compile(r"^[a-z][a-z0-9_.-]*$")
_PROFILE_RE = re.compile(r"^[a-z0-9][a-z0-9._/-]*$")
_DIGEST_RE = re.compile(r"^sha256:([0-9a-f]{64})$")
_TOP_LEVEL_KEYS = {
    "schema",
    "profile",
    "header",
    "max_packet",
    "entries",
    "digest",
}
_ENTRY_KEYS = {"name", "code", "semantic"}


def _canonical_bytes(document: Mapping[str, Any]) -> bytes:
    content = {key: value for key, value in document.items() if key != "digest"}
    try:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise RegistrySchemaError(
            "registry must contain only canonical JSON values"
        ) from exc


def canonical_digest(document: Mapping[str, Any]) -> str:
    """Return the canonical SHA-256 digest, excluding the ``digest`` member."""
    return "sha256:" + hashlib.sha256(_canonical_bytes(document)).hexdigest()


def _freeze(value: Any) -> Any:
    if isinstance(value, dict):
        return MappingProxyType({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, list):
        return tuple(_freeze(item) for item in value)
    return value


@dataclass(frozen=True)
class RegistryEntry:
    """A code and its domain-neutral semantic description."""

    name: str
    code: str
    semantic: Mapping[str, Any]


@dataclass(frozen=True)
class Registry:
    """A validated registry whose public state cannot be mutated."""

    schema: str
    profile: str
    header: str
    max_packet: int
    digest: str
    entries: tuple[RegistryEntry, ...]
    _by_name: Mapping[str, RegistryEntry]
    _by_code: Mapping[str, RegistryEntry]

    @classmethod
    def load(cls, path: str | Path) -> "Registry":
        """Load and validate a UTF-8 JSON registry artifact."""
        try:
            with Path(path).open(encoding="utf-8") as stream:
                document = json.load(stream)
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            raise RegistrySchemaError(f"cannot load registry: {exc}") from exc
        return cls.from_dict(document)

    @classmethod
    def from_dict(cls, document: Mapping[str, Any]) -> "Registry":
        """Validate and freeze an in-memory registry document."""
        if not isinstance(document, dict):
            raise RegistrySchemaError("registry root must be a JSON object")
        keys = set(document)
        if keys != _TOP_LEVEL_KEYS:
            missing = sorted(_TOP_LEVEL_KEYS - keys)
            unknown = sorted(keys - _TOP_LEVEL_KEYS)
            raise RegistrySchemaError(
                f"registry keys differ; missing={missing}, unknown={unknown}"
            )
        if document["schema"] != SCHEMA:
            raise RegistrySchemaError(f"unsupported registry schema: {document['schema']!r}")
        profile = document["profile"]
        if not isinstance(profile, str) or not _PROFILE_RE.fullmatch(profile):
            raise RegistrySchemaError(
                "profile must be a lowercase ASCII profile identifier"
            )
        header = document["header"]
        if not isinstance(header, str) or not _HEADER_RE.fullmatch(header):
            raise RegistrySchemaError("header must match M36[A-Z0-9]+")
        if len(header) + 11 > 36:
            raise RegistrySchemaError("header leaves no room for code and trace")
        if document["max_packet"] != 36 or isinstance(document["max_packet"], bool):
            raise RegistrySchemaError("max_packet must be the integer 36")
        supplied_digest = document["digest"]
        if not isinstance(supplied_digest, str) or not _DIGEST_RE.fullmatch(
            supplied_digest
        ):
            raise RegistrySchemaError("digest must be sha256: followed by 64 lowercase hex digits")
        expected_digest = canonical_digest(document)
        if supplied_digest != expected_digest:
            raise RegistryDigestError(
                f"registry digest mismatch: expected {expected_digest}, got {supplied_digest}"
            )
        raw_entries = document["entries"]
        if not isinstance(raw_entries, list) or not raw_entries:
            raise RegistrySchemaError("entries must be a non-empty array")

        entries: list[RegistryEntry] = []
        names: set[str] = set()
        codes: set[str] = set()
        for index, raw_entry in enumerate(raw_entries):
            if not isinstance(raw_entry, dict) or set(raw_entry) != _ENTRY_KEYS:
                raise RegistrySchemaError(
                    f"entry {index} must contain exactly name, code, and semantic"
                )
            name = raw_entry["name"]
            code = raw_entry["code"]
            semantic = raw_entry["semantic"]
            if not isinstance(name, str) or not _NAME_RE.fullmatch(name):
                raise RegistrySchemaError(f"entry {index} has invalid name")
            if not isinstance(code, str) or not _CODE_RE.fullmatch(code):
                raise RegistrySchemaError(
                    f"entry {index} code must be three uppercase ASCII alphanumerics"
                )
            if name in names:
                raise RegistrySchemaError(f"duplicate entry name: {name}")
            if code in codes:
                raise RegistrySchemaError(f"duplicate entry code: {code}")
            if not isinstance(semantic, dict) or not semantic:
                raise RegistrySchemaError(
                    f"entry {index} semantic must be a non-empty object"
                )
            names.add(name)
            codes.add(code)
            entries.append(RegistryEntry(name, code, _freeze(semantic)))

        by_name = MappingProxyType({entry.name: entry for entry in entries})
        by_code = MappingProxyType({entry.code: entry for entry in entries})
        return cls(
            schema=SCHEMA,
            profile=profile,
            header=header,
            max_packet=36,
            digest=supplied_digest,
            entries=tuple(entries),
            _by_name=by_name,
            _by_code=by_code,
        )

    def entry_for_name(self, name: str) -> RegistryEntry | None:
        return self._by_name.get(name)

    def entry_for_code(self, code: str) -> RegistryEntry | None:
        return self._by_code.get(code)
