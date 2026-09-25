# Morse/36 Specification

**Status:** Draft pre-v0.1  
**Category:** Compact Machine Intent (CMI)

## 1. Purpose

Morse/36 explores a compact, deterministic representation of machine intent.

The protocol is based on a deliberately narrow premise: when two machines share a vocabulary, they should not have to repeatedly transmit verbose descriptions of that vocabulary in order to communicate an action.

Morse/36 therefore optimizes for **intent**, not arbitrary document representation.

## 2. Design target

A conforming implementation SHOULD attempt to represent routine machine intents within an **M36** frame.

An M36 frame MUST NOT exceed 36 characters in its canonical textual representation.

When an intent cannot be represented faithfully within M36, an implementation MAY use an **M366** extended frame, whose canonical textual representation MUST NOT exceed 366 characters.

These limits are experimental constraints. The byte-level stable wire representation remains subject to RFC review.

## 3. Preliminary grammar

Pre-v0.1 uses a human-readable pipe-delimited notation:

```text
<route>|<intent>|<verb>|<argument>
```

Example:

```text
ASD|VCE|GET|001
```

The fields above are provisional. Their registry meanings MUST NOT be assumed until registered by an accepted RFC.

### 3.1 Route

A short registered identifier describing the communicating domain, service pair, or namespace.

### 3.2 Intent

A registered semantic identifier for the resource, capability, or intent class.

### 3.3 Verb

A deterministic operation identifier.

### 3.4 Argument

An optional compact value, registry value, reference, or parameter.

## 4. Canonicalization goals

A stable Morse/36 specification MUST eventually guarantee that:

1. one semantic intent has one canonical representation for a given protocol version;
2. equivalent implementations produce identical canonical frames;
3. a decoder can reject malformed or ambiguous frames deterministically;
4. unknown registry values fail explicitly rather than being guessed;
5. protocol extensions cannot silently redefine existing semantics.

## 5. Encoding

The experimental textual profile SHOULD use printable ASCII wherever possible so that character count and byte count remain easy to reason about during early benchmarking.

A stable RFC MUST define the exact permitted character set and wire encoding.

Until then, **36 characters MUST NOT be marketed as universally equivalent to 36 bytes**.

## 6. Transport independence

Morse/36 does not define physical or network transport.

A Morse/36 frame may be carried over transports including HTTP, QUIC, WebSocket, MQTT, message queues, local IPC, constrained radio, or future transports.

Transport framing and security overhead are outside the M36/M366 payload limits unless a future RFC explicitly says otherwise.

## 7. Registry

Canonical route, intent, verb, error, capability, and extension identifiers will be maintained in an open registry.

Registry assignments MUST be documented and versioned.

Private namespaces MAY exist, but they MUST NOT collide with reserved public identifiers.

## 8. Failure behavior

A decoder MUST NOT infer an unknown opcode using an LLM or probabilistic model and then present that inference as protocol truth.

Unknown, malformed, unsupported, or version-incompatible frames MUST produce deterministic failure states.

## 9. Security

Compactness must not remove authentication, authorization, integrity, replay protection, confidentiality, or transport security requirements.

Morse/36 represents intent. It does not grant permission to execute that intent.

## 10. Measurement

Protocol claims MUST be benchmarkable.

Benchmark 001 will measure representative workloads against suitable alternatives including JSON, compressed JSON, CBOR, and Protocol Buffers.

At minimum it will report payload size, encode/decode latency, semantic fidelity, failure behavior, and token consumption where an LLM is involved.

## 11. Compatibility

Pre-v0.1 is unstable.

No current field position, delimiter, opcode, or registry assignment is guaranteed to survive into v0.1.

Once a stable version exists, incompatible semantic changes MUST require an explicit protocol version change.

## 12. Principle

**Say only what the receiving machine needs to act, and never sacrifice meaning merely to save bytes.**
