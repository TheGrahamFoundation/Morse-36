# RFC-0001: Compact Machine Intent

**Status:** Draft  
**Protocol:** Morse/36  
**Steward:** The Graham Foundation

## Abstract

Morse/36 explores whether machine communication can separate **representation**, **semantic intent**, and **wire encoding**.

The current canonical model is:

```text
JSON / XML / HL7 / objects / language
                ↓
              FTIP
      canonical semantic intent
                ↓
        Morse/36 word(s)
                ↓
            transport
```

The receiver performs the reverse transformation: Morse/36 word(s) → FTIP → receiver-native operation.

## Hypothesis

When two systems share deterministic semantics, they may not need to repeatedly transmit descriptive structure. A source payload can be normalized into FTIP, and FTIP can be represented by compact registered word(s).

Morse/36 therefore does **not** claim to compress JSON. It asks whether normalized intent can have a smaller deterministic representation than repeatedly transmitting the source representation.

## FTIP

FTIP is the semantic boundary. It captures the meaning that must survive changes in source format and receiver implementation.

Equivalent source representations SHOULD be capable of producing equivalent FTIP intent. FTIP is then encoded through a versioned deterministic registry into Morse/36 word(s).

## Morse/36 words

A Morse/36 word is a registered deterministic reference to FTIP semantics. One intent MAY require multiple words. The exact alphabet, grammar and composition rules remain pre-v0.1 research work.

Old tuple/opcode examples are not part of the current proposal.

## M36 and M366

- **M36:** experimental envelope up to 36 characters.
- **M366:** extended envelope up to 366 characters.

These constraints must never cause semantic loss. Information not shared by the receiver must still be transmitted or referenced.

## Non-goals

Morse/36 does not attempt to replace general data formats or network transports, encode arbitrary information into 36 characters, use probabilistic guesses for protocol truth, or claim efficiency without measurement.

## The 1% principle

Morse/36 SHALL be judged by measured outcomes. Benchmarking must include the cost of source parsing, FTIP normalization, registry state, word encoding/decoding, security and failure recovery.

If the result is zero measurable improvement, publish zero. If the result is one percent, that one percent belongs to everyone.

## Open standard

The FTIP model, word registry, reference codecs, conformance tests and benchmark methodology should remain openly inspectable and independently implementable.

## Next work

1. define FTIP canonicalization rules;
2. define the Morse/36 word alphabet and grammar;
3. define word composition and M36/M366 envelopes;
4. define the public word ⇄ FTIP registry;
5. define version negotiation, errors and acknowledgements;
6. define integrity/security binding;
7. publish conformance vectors;
8. run Benchmark 001.

## Closing

**Representation → FTIP → Morse/36 word(s).**

The goal is not to make machines cryptic. The goal is to make unnecessary representation unnecessary.
