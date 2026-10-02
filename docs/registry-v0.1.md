# Morse/36 Registry — pre-v0.1

The registry binds **Morse/36 word(s)** to canonical **FTIP semantics**.

## Rule

```text
Morse/36 word(s) ⇄ FTIP semantic intent
```

The registry does not expose source-format field names and does not require the wire to carry route/action/resource tuples.

## Compiled artifact shape

The Python library accepts JSON artifacts with this exact top-level shape:

```json
{
  "schema": "morse36.registry/v1",
  "profile": "example-codec-a",
  "header": "M36A",
  "max_packet": 36,
  "entries": [
    {
      "name": "example.signal",
      "code": "EX1",
      "semantic": {"intent": "signal"}
    }
  ],
  "digest": "sha256:<64 lowercase hexadecimal characters>"
}
```

Names are stable lowercase identifiers. Codes are unique, uppercase,
three-character ASCII alphanumerics. `semantic` is a non-empty JSON object.
The header identifies the wire profile and `max_packet` is exactly 36.

The digest is SHA-256 over UTF-8 JSON after removing `digest`, sorting object
keys, disabling insignificant whitespace, and preserving array order. NaN and
other non-JSON values are forbidden. Loaders reject schema violations,
duplicates, and digest mismatches before exposing an immutable registry.

## Word assignments

**No production word assignments are frozen yet.** Early endpoint/action/resource codes from the tuple-frame experiment are retained only in git history and MUST NOT be interpreted as current Morse/36 wire syntax.

The first public registry RFC should define broader word composition and
reserved namespaces before assigning canonical public words.

## Governance

Published registry releases are immutable. A word MUST NOT silently change FTIP meaning. Any incompatible semantic change requires a new word or registry version and explicit peer negotiation.

Private dictionaries belong in Fox or equivalent domain compilers. Those
compilers may emit immutable compiled registry artifacts for authorized peers,
but private assignments are not embedded in the open Morse library. Morse owns
wire semantics; domain compilers own domain mapping.
