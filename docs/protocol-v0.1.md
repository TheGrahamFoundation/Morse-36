# Morse/36 Protocol Definition

Status: **pre-v0.1 research draft**

## 1. Purpose

Morse/36 tests whether machines can exchange normalized intent through compact deterministic **word(s)** rather than repeatedly transmitting verbose source representations.

## 2. Layer model

```text
Source Representation → FTIP → Morse/36 Word(s) → Transport
Transport → Morse/36 Word(s) → FTIP → Native Action
```

Source representation and wire representation are separate layers. JSON, XML, YAML, HL7, objects and natural language are inputs to semantic normalization; they are not Morse/36 syntax.

## 3. FTIP

FTIP is the canonical semantic intent layer. An encoder MUST resolve the source representation into FTIP before Morse/36 encoding. Equivalent source representations SHOULD normalize to equivalent FTIP intent.

FTIP is not transmitted merely because the encoder used it internally. The wire representation is Morse/36 word(s).

## 4. Morse/36 words

A Morse/36 word is a deterministic registry-bound representation of FTIP semantics. One intent MAY require a composition of words.

The old fixed-field tuple layout and examples such as `ASD|VCE|GET|001` or `0QALFRSOPHGETDIAGGCP00000100A1000000` are retired research sketches and are **not** current wire syntax.

The exact word alphabet, grammar, boundaries and registry mapping remain open pre-v0.1 work.

## 5. Envelopes

- **M36:** target maximum 36 characters for routine intent.
- **M366:** target maximum 366 characters when additional context is required.

An encoder MUST NOT discard semantic information merely to satisfy an envelope. Non-shared data must travel separately or by an authenticated reference.

## 6. Encoding pipeline

1. Parse the source representation without executing it.
2. Normalize meaning into FTIP.
3. Validate that FTIP is supported and authorized for encoding.
4. Resolve FTIP against the negotiated immutable registry.
5. Emit canonical Morse/36 word(s).
6. Bind required integrity/security metadata at the appropriate transport or companion layer.
7. Transmit.

A model MAY assist semantic normalization, but deterministic validation MUST accept or reject the final FTIP and word sequence.

## 7. Decoding pipeline

1. Parse Morse/36 word boundaries.
2. Verify protocol/registry compatibility.
3. Reject unknown or malformed words.
4. Resolve word(s) deterministically to FTIP.
5. Apply authentication, authorization, replay and safety policy.
6. Adapt FTIP to the receiver-native operation.
7. Execute only through the receiver's normal policy boundary.

## 8. Registry negotiation

Peers MUST agree on protocol version and an immutable registry identity/digest before interpreting words. A word MUST NOT silently change meaning between registry versions.

## 9. Non-goals

Morse/36 is not universal data compression, not a replacement for transport protocols, and not probabilistic authorization.

## 10. Open questions

- What word alphabet gives the best balance of compactness and inspectability?
- How are multiple words composed canonically?
- Which FTIP intents deserve public registry words?
- How should references and arguments be represented without leaking the old tuple abstraction onto the wire?
- What security binding preserves the word model without weakening authentication?
