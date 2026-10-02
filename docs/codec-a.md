# Experimental Codec A — Control Plane

**Status:** Experimental / dogfood  
**Envelope:** M36  
**Maximum:** 36 characters

Codec A is a registry-driven experimental implementation of Morse/36. It is
**not** the final public Morse/36 grammar.

## Layout

```text
M36A + III + TTTTTTTT + ARG
```

- `M36A` — self-identifying Morse/36 Codec A header
- `III` — registered three-character intent
- `TTTTTTTT` — deterministic eight-character trace fingerprint
- `ARG` — optional compact argument
- entire packet MUST be <= 36 characters

## Registries

Codec A contains no private code assignments. The three-character code is
resolved through an immutable, canonical-SHA-256-bound registry selected by the
application. Private dictionaries belong in Fox/domain compilers, not in
Morse/36. They are distributed to compatible peers as immutable compiled
registry artifacts.

Morse owns the envelope, trace fingerprint, argument canonicalization,
deterministic decoding, and failure semantics. A domain compiler owns the
mapping from private domain meaning to registry entries.

## Security boundary

Codec A carries **intent only**. It MUST NOT carry card details, access tokens,
Stripe secrets, OAuth credentials, or other payment/authentication secrets.

The eight-character BLAKE2s value is a trace fingerprint, not the full
idempotency key and not proof of identity. The library can verify a caller-held
full key against that fingerprint. It makes no authentication or authorization
claims; those controls remain the responsibility of the transport and
application layers.
