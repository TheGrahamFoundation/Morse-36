# Morse/36

Morse/36 is an experimental fixed-width protocol for deterministic agent-to-agent instructions.

Instead of repeatedly transmitting verbose task descriptions, two agents that share a versioned registry can exchange a 36-character Base36 frame. The frame identifies the sender, receiver, action, resource, context, referenced state, replay nonce, and an authentication hint.

> Morse/36 is a research proposal, not a production security protocol.

## Canonical frame

```text
0QALFRSOPHGETDIAGGCP00000100A1000000
```

```text
0 | Q | ALFR | SOPH | GET | DIAG | GCP0 | 00001 | 00A1 | 000000
V   K   SRC    DST    ACT   RES    CTX    REF     NONCE  AUTH
```

The example asks Sophia to retrieve Alfred's GCP diagnostic context. Field semantics are resolved against a shared registry snapshot.

## Repository map

- [`docs/protocol-v0.1.md`](docs/protocol-v0.1.md): normative draft
- [`docs/registry-v0.1.md`](docs/registry-v0.1.md): initial shared vocabulary
- [`docs/security.md`](docs/security.md): threat model and authentication limits
- [`docs/research-plan.md`](docs/research-plan.md): falsifiable test plan
- [`CONTRIBUTING.md`](CONTRIBUTING.md): public research workflow

## Central hypothesis

A compact frame can reduce bandwidth and parsing cost for repeated, well-known agent operations when both parties share deterministic registries and state. It cannot losslessly replace arbitrary JSON or natural language without that shared context.

## Status

`v0.1-draft` — open for criticism, experiments, and competing designs.

Morse/36 is maintained under The Graham Foundation and initiated by David Labs.
