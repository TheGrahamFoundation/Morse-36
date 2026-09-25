# Morse/36 Wire Model

## Representation → FTIP → Morse/36 word(s)

Morse/36 does **not** compress JSON, XML, YAML, HL7, or arbitrary text into shorter field names.

The canonical layering is:

```text
APPLICATION / DOMAIN REPRESENTATION
JSON · XML · YAML · HL7 · objects · language
                  |
                  v
                FTIP
        canonical semantic intent
                  |
                  v
          Morse/36 word(s)
                  |
================ WIRE ================
          Morse/36 word(s)
======================================
                  |
                  v
                FTIP
                  |
                  v
       receiver-native operation
```

## FTIP

FTIP belongs **between representation and Morse/36 encoding**. It is not the wire word and it is not an abbreviation of the source payload.

Its job is semantic normalization: different source formats that mean the same thing should be capable of resolving to the same FTIP intent.

Conceptually:

```text
JSON ─┐
XML  ─┼─→ FTIP ─→ Morse/36 word(s)
HL7  ─┤
RAW  ─┘
```

The reverse path resolves received word(s) back to FTIP before adapting that intent to the receiver's native API, object model, device command, or domain representation.

## Morse/36 words

A Morse/36 word is a compact deterministic reference to shared FTIP semantics. A complete intent may use one word or a composition of words.

The exact pre-v0.1 word grammar is still under research. Internal opcodes, tuples, parse trees, DLM state and source schemas MUST NOT be exposed merely because an encoder used them.

## M36 and M366

**M36** is the compact envelope, targeting no more than 36 characters. **M366** is the extended envelope for intents that require additional context.

Neither envelope permits semantic loss merely to satisfy the length limit.

## Canonical principle

> **Morse/36 does not compress content. Morse/36 encodes normalized intent as word(s).**

## Open question

How much source representation can safely disappear after FTIP normalization when two machines share deterministic semantics?
