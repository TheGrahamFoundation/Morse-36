# Research Plan

## Research question

Can a shared-registry, 36-character instruction frame reduce agent-to-agent communication cost while preserving semantic accuracy, operational safety, and debuggability?

## Hypotheses

1. For repeated registered tasks, Morse/36 reduces transmitted bytes and parser work compared with canonical JSON.
2. Deterministic validation prevents unsupported model-generated instructions from reaching execution.
3. Registry drift is the dominant semantic failure mode.
4. A 36-character frame is insufficient as a standalone secure envelope.

## Baselines

- canonical JSON tool call;
- compact JSON;
- CBOR or MessagePack;
- direct function/RPC identifier plus arguments;
- Morse/36 with and without companion payloads.

## Measurements

- wire bytes per completed task;
- tokens consumed in encode/decode steps;
- p50, p95, and p99 latency;
- exact semantic match rate;
- false execution and false rejection rates;
- registry miss and drift rate;
- replay rejection rate;
- recovery behavior after corruption;
- implementation and debugging complexity.

## Initial test bed

Use two isolated agents with a pinned registry. Start with read-only synthetic operations under `TEST`; do not use production credentials or infrastructure.

Test phases:

1. deterministic codec round trips;
2. corruption and invalid-length rejection;
3. unknown-code and mismatched-registry rejection;
4. replay and idempotency trials;
5. DLM-assisted intent mapping with deterministic validation;
6. comparison against baselines;
7. adversarial and fuzz testing;
8. multi-agent routing and registry upgrade trials.

## Success criteria for further research

- 100% round-trip accuracy for registered deterministic vectors;
- zero execution of malformed, unauthorized, or unknown frames;
- measurable byte reduction for the selected workload;
- no material latency regression against the chosen baseline;
- reproducible results across at least two independent implementations.

Failure to meet these criteria is a valid research result and MUST be documented.

## Canonical vector 0001

```text
Frame: 0QALFRSOPHGETDIAGGCP00000100A1000000
Length: 36
Meaning: Alfred queries Sophia for diagnostic record 00001 in GCP0.
Security: Unsigned demonstration vector; it must not execute outside local TEST mode.
```
