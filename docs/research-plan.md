# Research Plan

## Research question

Can the pipeline **source representation → FTIP → Morse/36 word(s)** reduce machine-to-machine communication cost while preserving exact semantic intent, safety and debuggability?

## Hypotheses

1. Different source formats expressing equivalent meaning can normalize to the same FTIP intent.
2. Registered FTIP intents can be represented by compact Morse/36 word(s) with exact round-trip semantics.
3. Registry drift is a primary semantic failure mode and must fail closed.
4. Compact words do not remove the need for external authentication, authorization and replay protection.

## Baselines

- canonical JSON tool call;
- compact/compressed JSON;
- CBOR or MessagePack;
- direct RPC/function identifiers;
- FTIP + Morse/36 word(s), including registry overhead.

## Measurements

Measure source bytes, FTIP normalization latency, Morse word bytes, encode/decode latency, semantic match rate, registry miss/drift rate, false execution/rejection, and implementation complexity.

## Test phases

1. source-format → FTIP equivalence tests;
2. FTIP → word → FTIP deterministic round trips;
3. malformed and unknown-word rejection;
4. registry mismatch trials;
5. replay/idempotency and security integration;
6. baseline comparison;
7. fuzz and adversarial testing;
8. independent implementation reproduction.

## Success criteria

- 100% semantic round-trip accuracy for registered deterministic vectors;
- zero execution of unknown or unauthorized words;
- measurable benefit for at least one defined workload;
- reproducible results across at least two implementations.

Failure is a valid result and MUST be documented.

## Vector 0001

```text
Source: JSON describing Alfred requesting Sophia to diagnose voice
FTIP:   alfred>sophia:request.diagnostic(voice)
M36:    <registry-assigned word pending>
```

The word is intentionally unassigned until the word grammar and registry RFC are accepted.
