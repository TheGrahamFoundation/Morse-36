# Security Model

Morse/36 shortens instructions; it does not remove the need for identity, authorization, confidentiality, or audit controls.

## Threats considered

- forged source identifiers;
- frame tampering;
- replay and duplicate execution;
- registry downgrade or drift;
- reference substitution;
- malicious or compromised encoder models;
- unauthorized commands;
- traffic analysis.

## AUTH limitation

Six Base36 characters represent approximately 31 bits. A truncated tag of that size is useful for corruption detection and controlled experiments, but it is too small to be the sole authenticator in an adversarial system.

`AUTH=000000` means unsigned and MUST be accepted only by an explicitly configured local test profile.

## Secure companion envelope

Privileged or networked operation requires an authenticated transport or a detached signature covering:

```text
frame || registry_digest || payload_digest || issued_at || expires_at || session_id
```

The envelope MUST identify the algorithm and key ID, carry the complete signature or MAC, bind any companion payload by digest, and use short expiries. The frame's six-character `AUTH` value MAY be a deterministic prefix/check value derived from the full authenticator, but verification of that prefix MUST NOT replace full verification.

The protocol does not mandate a cryptographic algorithm in v0.1. Candidate profiles should test HMAC-SHA-256 for mutually trusted services and Ed25519 signatures for independently verifiable senders.

## Authorization

Authentication answers who sent a frame. Authorization decides whether that sender may perform the tuple `(K, ACT, RES, CTX)` against `DST`.

- Decoders MUST fail closed on unknown codes.
- Model output MUST NOT grant permissions.
- Destructive actions require explicit target-side policy.
- Broadcast commands are disabled by default.
- `PROD` is prohibited in the initial test bed.
- Every decoded and rejected frame SHOULD produce an append-only audit event.

## Registry integrity

Peers MUST negotiate an immutable registry digest before interpreting codes. A registry update is data-plane incompatible until both peers explicitly adopt it. Downgrade attempts MUST be logged and rejected unless a documented compatibility profile allows them.

## Research warning

Do not use v0.1 to control safety-critical systems, financial transfers, production infrastructure, weapons, emergency response, or access-control decisions.
