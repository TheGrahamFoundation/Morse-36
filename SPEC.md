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

A source representation MAY be JSON, XML, YAML, HL7, an object graph, natural language, another domain format, or an existing Morse/36 package.

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

These are experimental envelopes, not a requirement to destroy meaning to meet a length target. An M36 word MAY therefore be shorter than 36 characters; 36 is an envelope ceiling, not a padding requirement.

### 4.1 Self-describing packaging

A valid Morse/36 wire representation MUST identify itself as Morse/36 packaging and MUST carry enough deterministic metadata for a compatible decoder to select the required codec/registry version. The decoder MUST NOT require out-of-band knowledge merely to determine that the received object is Morse/36.

Conceptually:

```text
M36 envelope → protocol identity + codec/version + payload
```

The exact compact grammar for this metadata remains an RFC item. The metadata MUST be deterministic and MUST NOT rely on probabilistic inference.

### 4.2 Recursive Morse / re-Morsing

The payload of an M36 envelope MAY itself be a Morse/36 representation. Encoding an already-Morsed object is called **re-Morsing**.

```text
source
  ↓ Morse/36
Morse₁
  ↓ Morse/36
Morse₂
  ↓ Morse/36
Morse₃
```

A decoder receiving `Morse₃` MUST be able to identify and unwrap the outer M36 package. If the recovered payload is itself valid M36 packaging, decoding MAY continue recursively until the terminal payload is reached or an explicitly requested layer is reached.

Morse-1, Morse-2, and later re-Morsed layers do not require separate protocols. **The package itself declares how it is to be interpreted.**

Implementations MUST impose a configurable maximum recursion depth and MUST fail explicitly when that limit is exceeded, preventing malformed or hostile infinitely nested input from causing unbounded decoding.

### 4.3 Encoding is not encryption

Morsing and re-Morsing are encoding operations. Reversibility or multiple encoding layers MUST NOT be described as encryption unless a defined cryptographic confidentiality mechanism is separately applied.

## 5. Canonicalization goals

A stable specification MUST guarantee that, for a given protocol and registry version:

1. equivalent FTIP intent produces the same canonical Morse word sequence;
2. a word sequence resolves to one defined FTIP meaning;
3. malformed, unknown or ambiguous words fail explicitly;
4. extensions cannot silently redefine existing words;
5. source formats do not alter the meaning after FTIP normalization;
6. every self-described M36 layer can be deterministically recognized and decoded by a compatible implementation.

## 6. Transport independence

Morse/36 does not define transport. Words may travel over HTTP, QUIC, WebSocket, MQTT, queues, IPC, radio, or other transports.

## 7. Registry

The open registry binds Morse words to FTIP semantics. Registry releases MUST be immutable and versioned. Private namespaces MAY exist but MUST NOT collide with reserved public assignments.

## 8. Failure behavior

A decoder MUST NOT probabilistically guess an unknown Morse word and present the guess as protocol truth. Unknown, malformed, unsupported, version-incompatible, or recursion-limit-exceeding words MUST fail deterministically.

## 9. Security

Morse/36 represents intent; it does not grant permission to execute intent. Authentication, authorization, integrity, replay protection and confidentiality remain required at the appropriate layer.

Recursive packaging MUST NOT be treated as a security boundary or confidentiality mechanism.

## 10. Measurement

Benchmark 001 MUST distinguish:

- source representation size;
- FTIP normalization cost;
- Morse/36 word size;
- registry/version overhead;
- encode/decode latency;
- semantic fidelity;
- failure behavior;
- recursive packaging depth and per-layer overhead where re-Morsing is used.

Morse/36 MUST NOT be described as JSON compression. It is an intent encoding experiment.

## 11. Principle

**Representation → meaning → word. Never confuse the three layers.**

A second invariant applies to packaging:

**Anything can be Morsed. Anything Morsed can be re-Morsed. The package tells the decoder how to come back.**
