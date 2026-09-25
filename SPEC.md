# Morse/36 Specification

**Status:** Draft pre-v0.1  
**Category:** Compact Machine Intent (CMI)

## 1. Purpose

Morse/36 explores a compact deterministic representation of machine intent. The protocol separates **source representation**, **semantic intent**, and **wire representation**.

## 2. Canonical pipeline

```text
source representation → FTIP → Morse/36 word(s) → transport
transport → Morse/36 word(s) → FTIP → receiver-native action
```

A source representation MAY be JSON, XML, YAML, HL7, an object graph, natural language, or another domain format.

**FTIP** is the canonical semantic intent layer. It contains the meaning that must survive representation changes.

A **Morse/36 word** is a deterministic registered encoding of FTIP semantics. One FTIP intent MAY require one or more words.

## 3. Word model

Pre-v0.1 no longer defines a public pipe-delimited route/verb/argument tuple. Tuple-looking forms such as `ASD|VCE|GET|001` are obsolete examples and MUST NOT be treated as Morse/36 wire syntax.

The stable word grammar remains an open RFC item. A future grammar MUST define:

- permitted alphabet and canonical case;
- word boundaries and composition;
- registry/version binding;
- canonical mapping from FTIP to word(s);
- references for information that cannot be represented by shared semantics;
- acknowledgement and error words;
- integrity and security binding.

## 4. Frame envelopes

An **M36** representation SHOULD fit within 36 characters. If faithful intent requires more context, an implementation MAY use **M366**, up to 366 characters.

These are experimental envelopes, not a requirement to destroy meaning to meet a length target.

## 5. Canonicalization goals

A stable specification MUST guarantee that, for a given protocol and registry version:

1. equivalent FTIP intent produces the same canonical Morse word sequence;
2. a word sequence resolves to one defined FTIP meaning;
3. malformed, unknown or ambiguous words fail explicitly;
4. extensions cannot silently redefine existing words;
5. source formats do not alter the meaning after FTIP normalization.

## 6. Transport independence

Morse/36 does not define transport. Words may travel over HTTP, QUIC, WebSocket, MQTT, queues, IPC, radio, or other transports.

## 7. Registry

The open registry binds Morse words to FTIP semantics. Registry releases MUST be immutable and versioned. Private namespaces MAY exist but MUST NOT collide with reserved public assignments.

## 8. Failure behavior

A decoder MUST NOT probabilistically guess an unknown Morse word and present the guess as protocol truth. Unknown, malformed, unsupported, or version-incompatible words MUST fail deterministically.

## 9. Security

Morse/36 represents intent; it does not grant permission to execute intent. Authentication, authorization, integrity, replay protection and confidentiality remain required at the appropriate layer.

## 10. Measurement

Benchmark 001 MUST distinguish:

- source representation size;
- FTIP normalization cost;
- Morse/36 word size;
- registry/version overhead;
- encode/decode latency;
- semantic fidelity;
- failure behavior.

Morse/36 MUST NOT be described as JSON compression. It is an intent encoding experiment.

## 11. Principle

**Representation → meaning → word. Never confuse the three layers.**
