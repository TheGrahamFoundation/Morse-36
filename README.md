# Morse/36

**Compact Machine Intent.**

Morse/36 is an open protocol experiment for expressing machine intent in a compact, deterministic, implementation-independent form.

It asks a simple question:

> How little does one machine need to say for another machine to act correctly?

Morse/36 is stewarded by **The Graham Foundation**. Implementations may be built by anyone.

## Why

Machine-to-machine systems commonly exchange self-describing payloads using formats such as JSON, XML, CBOR, MessagePack, or Protocol Buffers. Those formats are excellent at representing data.

Morse/36 explores a narrower problem: **intent**.

An agent often does not need a paragraph, a verbose object, or repeated field names to tell another agent what it wants. If both sides share a deterministic vocabulary, the intent itself can be represented compactly.

Morse/36 calls this **Compact Machine Intent (CMI)**.

## Model

```text
Human / System Intent
        |
        v
   Intent Encoder
        |
        v
     Morse/36
        |
        v
 HTTP / QUIC / MQTT / WebSocket / Radio / ...
        |
        v
   Intent Decoder
        |
        v
 Machine / Agent / Service / Device
```

Morse/36 is not a transport protocol. It can travel over existing transports.

## Frames

The protocol begins with two intentionally constrained frame classes:

- **M36** — compact intent frame, targeting a maximum of 36 characters.
- **M366** — extended intent frame, targeting a maximum of 366 characters when additional context is required.

The limits are design constraints, not claims of optimality. The specification will define the exact byte-level representation before a stable release.

## Example

A verbose representation might express:

```json
{
  "source": "alfred",
  "destination": "sophia",
  "operation": "diagnostic",
  "resource": "voice",
  "status": "request"
}
```

A future Morse/36 registry could assign canonical semantics allowing an equivalent intent to be expressed approximately as:

```text
ASD|VCE|GET|001
```

This example is illustrative. Opcode assignments are not stable until they enter the public registry specification.

## Design principles

1. **Intent over description** — transmit what the receiver needs in order to act.
2. **Deterministic semantics** — the same valid frame must have the same defined meaning.
3. **Bounded representation** — frame classes have explicit limits.
4. **Transport independence** — Morse/36 should work above multiple transports.
5. **Implementation independence** — no David Labs or Foundation service should be required to implement the standard.
6. **Open registry** — canonical meanings, namespaces, and extensions must be publicly specified.
7. **Measurable claims** — compactness, latency, token usage, and semantic fidelity must be benchmarked rather than assumed.

## What Morse/36 is not

Morse/36 is not intended to replace JSON or XML universally. It is not an LLM prompt format, and it is not itself a networking transport.

It is an experiment toward a standard vocabulary and wire representation for **compact machine intent**.

## Road to v0.1

Before the protocol is considered usable, the project must define:

- character and byte encoding
- grammar and canonicalization
- addressing and namespaces
- intent/opcode registry
- argument representation
- M36 and M366 framing
- version negotiation
- errors and acknowledgements
- extension mechanism
- integrity/security considerations
- compatibility rules
- reference encoder and decoder
- conformance tests
- benchmarks against appropriate alternatives

## Benchmark 001

The first benchmark will compare representative machine/agent messages across JSON, compressed JSON, CBOR, Protocol Buffers, and Morse/36.

Measurements should include:

- bytes on the wire at the payload layer
- encoded/compressed size where applicable
- encode/decode latency
- parser complexity
- LLM token consumption where relevant
- semantic fidelity
- failure behavior

The goal is not to manufacture a win. The goal is to discover where Compact Machine Intent is actually useful.

## Governance

Morse/36 is intended to evolve through an open specification and RFC process under The Graham Foundation.

No proprietary David Labs infrastructure is required by the protocol.

The registry, reference implementations, conformance suite, and benchmark methodology should remain inspectable and reproducible.

## Status

**Experimental / pre-v0.1.**

Nothing in the current repository should yet be treated as a stable wire standard.

---

**Morse/36 — Compact Machine Intent.**
