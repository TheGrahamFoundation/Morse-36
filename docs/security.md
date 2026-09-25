# Security Model

Morse/36 word(s) represent intent; they do not grant permission to execute intent.

## Threats

- forged sender identity;
- word tampering or substitution;
- replay and duplicate execution;
- registry downgrade or drift;
- malicious FTIP normalization;
- unauthorized intent;
- traffic analysis.

## Authorization boundary

Authentication answers who sent the message. Authorization decides whether that sender may perform the **FTIP intent resolved from the received Morse/36 word(s)**.

- Unknown words MUST fail closed.
- Unknown FTIP mappings MUST fail closed.
- Model output MUST NOT grant permissions.
- Destructive operations require explicit target-side policy.
- Every accepted and rejected word sequence SHOULD be auditable with its registry version.

## Integrity

The compact word representation is not required to contain a complete cryptographic authenticator. Networked or privileged use requires authenticated transport or a companion signature/MAC that binds at minimum:

```text
morse_words || registry_digest || payload_digest || issued_at || expires_at || session_id
```

## Registry integrity

Peers MUST agree on an immutable registry identity/digest before interpreting words. A registry update is incompatible until both peers explicitly adopt it. A word MUST NOT silently acquire a different FTIP meaning.

## FTIP safety

If probabilistic inference is used to derive FTIP from source content, a deterministic validator MUST accept or reject the resulting FTIP before encoding. On decode, Morse words resolve deterministically to FTIP; an LLM MUST NOT guess the meaning of an unknown word.

## Research warning

Pre-v0.1 is experimental and should not control safety-critical or high-consequence systems.
