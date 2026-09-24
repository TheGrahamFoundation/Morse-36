# RFC-0001: Compact Machine Intent

**Status:** Draft  
**Protocol:** Morse/36  
**Steward:** The Graham Foundation

## Abstract

This RFC proposes **Compact Machine Intent (CMI)** as the problem domain addressed by Morse/36.

Modern machine communication frequently uses formats designed to represent general-purpose structured data. That flexibility is valuable, but many machine-to-machine interactions are much narrower: a sender wants a receiver to perform, acknowledge, inspect, report, or refuse a known operation.

When both sides already share a deterministic semantic registry, repeatedly transmitting descriptive structure may be unnecessary.

Morse/36 asks whether machine intent can be represented with materially less payload while remaining deterministic, inspectable, interoperable, and safe.

## Motivation

At planetary scale, software moves enormous quantities of information through networks, memory, storage systems, queues, logs, caches, and compute infrastructure.

Morse/36 does not begin with the assumption that it can transform that infrastructure.

It begins with a smaller obligation:

**Do not transmit information a machine does not need.**

If an open protocol can reduce the representation cost of applicable machine intents by even a small amount, and that reduction survives honest benchmarking at scale, the aggregate effect can matter.

A one-percent reduction is not dismissed as insignificant. In a sufficiently large system, one percent can mean less bandwidth moved, fewer bytes stored, less memory pressure, fewer resources consumed, and infrastructure that has to do slightly less work.

The project therefore defines success conservatively:

> If Morse/36 can produce a reproducible 1% reduction in the resources required for suitable machine-intent workloads, without sacrificing semantic fidelity, interoperability, reliability, or safety, it has achieved something useful for humanity.

This is a research target, not a claim that such savings have already been demonstrated.

## Proposal

Define an open, deterministic semantic vocabulary and bounded representation for machine intent.

The initial frame classes are:

- **M36:** up to 36 characters in the experimental canonical textual representation.
- **M366:** up to 366 characters for extended intent and context.

The protocol remains independent of transport and implementation.

## Non-goals

Morse/36 does not attempt to:

- replace JSON, XML, CBOR, or Protocol Buffers for general data representation;
- replace HTTP, QUIC, MQTT, WebSocket, or other transports;
- encode arbitrary human language into 36 characters;
- rely on probabilistic interpretation for protocol correctness;
- claim environmental or infrastructure savings without measurement.

## The Compact Machine Intent hypothesis

Consider two systems that already agree on:

- identities;
- operations;
- capabilities;
- schemas;
- error meanings;
- protocol version.

The hypothesis is that a significant subset of their communication can reference those shared semantics rather than repeatedly describe them.

Therefore:

```text
shared semantics + compact reference = machine intent
```

The receiver resolves the reference deterministically through the same versioned registry.

## Human inspectability

Early Morse/36 profiles remain textual because inspectability is useful while the protocol is being designed.

Binary representations may later be proposed, but they must demonstrate meaningful benefit and preserve deterministic tooling.

## The 1% principle

Morse/36 SHALL be judged by measured system outcomes rather than aesthetic compactness.

A smaller-looking string is not automatically a better protocol.

Any claimed reduction must account for the relevant workload and disclose the measurement boundary: payload, transport, storage, memory, compute, or complete system.

A change that saves bytes but materially increases compute, ambiguity, errors, or operational complexity may be a net loss.

The project's ambition is cumulative efficiency.

Millions or billions of small interactions can make small improvements meaningful.

## Open standard

The specification, registry, reference codecs, conformance tests, and benchmark methodology should be openly inspectable and implementable.

No Foundation-operated or David Labs-operated service is required to encode or decode Morse/36.

An implementation that conforms to the public specification is a Morse/36 implementation regardless of who built it.

## Next work

RFCs following this document should specify:

1. canonical character set and encoding;
2. exact M36 frame grammar;
3. M366 extension framing;
4. namespaces and addressing;
5. public semantic registry;
6. version negotiation;
7. acknowledgements and errors;
8. extension negotiation;
9. integrity and security considerations;
10. conformance test vectors;
11. Benchmark 001 methodology.

## Closing

Morse/36 is intentionally small.

The goal is not to make machines cryptic. The goal is to make unnecessary machine communication unnecessary.

If the result is zero measurable improvement, the benchmark should say so.

If the result is one percent, that one percent belongs to everyone.
