# Morse/36: Compact Machine Intent

## The wire should carry intent, not representation

Morse/36 does **not** compress JSON, XML, YAML, HL7, or arbitrary text into shorter field names.

Those formats may exist inside an application. They may remain the canonical representation of data at rest. Morse/36 addresses a different boundary: **what must actually cross the wire for another machine to understand the intended action?**

A Morse is layered.

```text
APPLICATION / DOMAIN CONTENT
HL7 · JSON · XML · YAML · objects · state
              |
              v
       semantic resolution
              |
              v
     Compact Machine Intent
              |
              v
       Morse word / words
              |
============== WIRE ==============
              |
             FTIP
              |
==================================
              |
              v
     deterministic resolution
              |
              v
        MACHINE ACTION
```

The structures used to derive a Morse are implementation details. They are not required to appear on the wire.

## FTIP

`FTIP` is the project's first deliberately abstract example of a Morse word.

It should be read as a demonstration of the model, not as a permanently assigned production opcode.

The important property is that the receiver does not need to receive the internal decomposition used by the sender. Both parties resolve the Morse through an agreed, versioned semantic contract.

## Healthcare example

Healthcare makes the distinction easy to see.

A healthcare system may internally represent an event using HL7. Another system may also understand HL7. Morse/36 does not claim HL7 is unnecessary.

It asks whether the entire HL7 representation must cross a particular machine-to-machine boundary when the receiver already possesses the relevant state and only needs to understand the intended operation.

Conceptually:

```text
SYSTEM A                              SYSTEM B

HL7 / domain state                   HL7 / domain state
       |                                    ^
       v                                    |
Morse semantic encoder               Morse semantic decoder
       |                                    ^
       +--------------- FTIP ---------------+
                         WIRE
```

If the receiver does **not** already possess information required to execute the intent, that information still has to be transferred or referenced. Morse/36 does not violate information theory and must never pretend otherwise.

## Canonical principle

> **Morse/36 does not compress content. Morse/36 compacts intent.**

A Morse word is therefore not merely an abbreviation of serialized fields. It is a deterministic reference to shared semantics.

## M36 and M366

An M36 frame carries one or more Morse words within the experimental 36-character envelope.

M366 provides a larger envelope for compositions requiring additional intent/context.

The visible wire representation remains Morse words. Internal parsing structures, semantic graphs, DLM state, schemas, and domain representations are not exposed merely because the encoder used them.

## Open question

The central research question is:

> How much representation can safely disappear from the wire when two machines share deterministic semantics?

That question should be answered through open discussion, implementations, and reproducible measurement.
