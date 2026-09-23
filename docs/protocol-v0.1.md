# Morse/36 Protocol Definition

Status: **v0.1 research draft**  
Normative words **MUST**, **MUST NOT**, **SHOULD**, and **MAY** describe requirements for experimental interoperability.

## 1. Purpose

Morse/36 tests whether agents can exchange common instructions through a compact, deterministic frame rather than a repeated verbose payload.

The protocol is designed for:

- repeated operations with shared semantics;
- constrained networks and edge devices;
- deterministic routing before probabilistic inference;
- auditable agent-to-agent experiments.

It is not designed to encode arbitrary information into 36 characters. Novel or high-entropy data MUST be transmitted separately and referenced by the frame.

## 2. Alphabet and serialization

A core frame MUST contain exactly 36 ASCII characters from:

```text
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

Lowercase input, whitespace, separators, and Unicode are invalid on the wire. Human interfaces MAY display separators but MUST remove them before transmission.

## 3. Fixed-width layout

| Offset | Width | Field | Meaning |
|---:|---:|---|---|
| 0 | 1 | `V` | Protocol major version |
| 1 | 1 | `K` | Message kind |
| 2 | 4 | `SRC` | Source agent identifier |
| 6 | 4 | `DST` | Destination agent or service |
| 10 | 3 | `ACT` | Requested action |
| 13 | 4 | `RES` | Resource or subject |
| 17 | 4 | `CTX` | Execution context |
| 21 | 5 | `REF` | Shared-state or payload reference |
| 26 | 4 | `NONCE` | Replay/deduplication value |
| 30 | 6 | `AUTH` | Truncated authentication hint |

Total width: **36 characters**.

## 4. Field rules

### V — version

`0` identifies this research draft. A decoder MUST reject unsupported versions; it MUST NOT silently reinterpret them.

### K — kind

Initial kinds are `Q` query, `C` command, `E` event, `R` response, `A` acknowledgement, `X` error, and `H` handshake.

### SRC and DST — endpoints

Four-character identifiers are registry entries, not free-form abbreviations. `FFFF` is broadcast and MUST be disabled unless the transport explicitly permits broadcast.

### ACT, RES, and CTX — instruction tuple

The tuple `(ACT, RES, CTX)` defines the deterministic instruction. A decoder MUST resolve all three values against the same registry version. Unknown codes MUST fail closed.

### REF — state reference

`REF` addresses a registry-defined record, cached payload, workflow state, or external companion payload. It is not globally unique. Its meaning is scoped by the negotiated registry and context.

`00000` means no referenced state.

### NONCE — replay and idempotency input

The sender increments or randomly assigns `NONCE` according to the active session profile. The receiver MUST maintain a replay window for privileged operations. Reusing a nonce MUST NOT make a non-idempotent operation execute twice.

### AUTH — authentication hint

`AUTH` is a six-character truncated tag used by the research prototype for rapid rejection and experiment measurement. It provides only about 31 bits of tag space and is **not sufficient authentication for hostile or production environments**.

Privileged operations MUST use the secure companion envelope defined in `security.md`.

## 5. Canonical example

```text
0QALFRSOPHGETDIAGGCP00000100A1000000
```

| Field | Value | Interpretation |
|---|---|---|
| `V` | `0` | Draft version |
| `K` | `Q` | Query |
| `SRC` | `ALFR` | Alfred |
| `DST` | `SOPH` | Sophia |
| `ACT` | `GET` | Retrieve |
| `RES` | `DIAG` | Diagnostic |
| `CTX` | `GCP0` | Google Cloud profile 0 |
| `REF` | `00001` | Shared record 1 |
| `NONCE` | `00A1` | Session nonce |
| `AUTH` | `000000` | Unsigned demonstration only |

## 6. Encoding pipeline

1. Normalize the intent without executing it.
2. Resolve source and destination identities.
3. Map intent to a registered `(K, ACT, RES, CTX)` tuple.
4. Store non-encodable data as companion state and assign `REF`.
5. Assign `NONCE` under the session replay policy.
6. Serialize the first 30 characters.
7. Calculate `AUTH` under the negotiated profile.
8. Validate length, alphabet, registry compatibility, authorization, and policy.
9. Transmit.

A DLM or LLM MAY propose a mapping, but a deterministic validator MUST produce or reject the final frame. Model output MUST NOT bypass registry and authorization checks.

## 7. Decoding pipeline

1. Reject frames that are not exactly 36 Base36 characters.
2. Split by fixed offsets.
3. Verify supported version and negotiated registry.
4. Verify the full companion signature when required, then verify `AUTH`.
5. Reject replayed or expired nonces.
6. Resolve every registry code; unknown values fail closed.
7. Apply authorization and safety policy.
8. Produce a typed instruction object.
9. Execute only through the target agent's normal policy boundary.

## 8. Responses and errors

Responses SHOULD reuse the request `REF` when it identifies the active transaction. `A` acknowledges acceptance, `R` returns a referenced result, and `X` returns a registered error class. Acknowledgement is not proof of successful task completion.

## 9. Registry negotiation

Before normal exchange, peers MUST agree on:

- protocol version;
- registry identifier and immutable digest;
- authentication profile;
- nonce and replay policy;
- maximum companion payload size;
- expiry and retry behavior.

Negotiation MAY occur through a verbose bootstrap transport. Compression begins only after both peers confirm the same state.

## 10. Non-goals for v0.1

- universal natural-language compression;
- replacement of all transport protocols;
- autonomous authorization by an inference model;
- production-grade cryptography inside 36 characters;
- guaranteed semantic compatibility without shared registries.

## 11. Open questions

- Is fixed width superior to a smaller binary representation plus printable encoding?
- Which instructions occur frequently enough to justify registry entries?
- How often does registry drift cause semantic failure?
- Does model-assisted encoding remain deterministic across vendors and versions?
- Which authentication design preserves compactness without weakening security?
