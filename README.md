# Morse/36

**Compact Machine Intent.**

> How little does one machine need to say for another machine to act correctly?

### [▶ OPEN THE INTERACTIVE MORSE/36 WORKBENCH](https://thegrahamfoundation.github.io/Morse-36/workbench/)

**Source → FTIP → Morse → Morse² → M36 Wire**

Use the live Workbench to enter a payload and watch it move layer by layer toward a bounded Morse/36 representation.

[Launch Workbench ↗](https://thegrahamfoundation.github.io/Morse-36/workbench/) · [Project Landing Page ↗](https://thegrahamfoundation.github.io/Morse-36/)

---

Morse/36 is an open protocol experiment for expressing normalized machine intent as compact, deterministic **Morse/36 word(s)**.

Morse/36 is stewarded by **The Graham Foundation**.

## Canonical model

```text
JSON / XML / YAML / HL7 / object / natural language
                    ↓
                  FTIP
          canonical semantic intent
                    ↓
            Morse/36 word(s)
                    ↓
 HTTP / QUIC / MQTT / WebSocket / Radio / ...
                    ↓
            Morse/36 word(s)
                    ↓
                  FTIP
                    ↓
       receiver-native action / data
```

**FTIP is the semantic intent layer. Morse/36 word(s) are the compact representation layer.**

Morse/36 does not compress JSON. A source representation is interpreted into FTIP; FTIP is then encoded into one or more Morse/36 words. Decoding reverses that path.

## Example

```json
{
  "source": "alfred",
  "destination": "sophia",
  "operation": "diagnostic",
  "resource": "voice",
  "status": "request"
}
```

Conceptually:

```text
JSON
  ↓
FTIP: Alfred → Sophia : request diagnostic of voice
  ↓
Morse/36 word(s)
```

The final word assignment is registry-defined. Old tuple/opcode demonstrations such as `ASD|VCE|GET|001` are obsolete and are not Morse/36 wire syntax.

## M36 and M366

- **M36** — one or more Morse words within an experimental maximum envelope of 36 characters.
- **M366** — extended composition, up to 366 characters when additional intent/context is required.

The limits are research constraints, not claims of optimality.

## Design principles

1. **Intent over representation** — source serialization is not the protocol.
2. **FTIP before encoding** — normalize meaning before producing Morse words.
3. **Words on the wire** — internal tuples, parse trees and model state remain implementation details.
4. **Deterministic semantics** — a registered word has one defined meaning for a registry version.
5. **Transport independence** — Morse/36 rides above existing transports.
6. **Open registry** — word meanings and extensions are versioned and inspectable.
7. **Measurable claims** — benchmark semantic fidelity, bytes, latency and failure behavior.

## What Morse/36 is not

Morse/36 is not a universal replacement for JSON, XML, protobuf or transport protocols. It is not an LLM prompt format. It does not make information disappear: data not already shared by the receiver must still travel or be referenced.

## Status

**Experimental / pre-v0.1.** Word grammar and registry assignments are not stable yet.

See `SPEC.md`, `docs/WIRE-MODEL.md`, and the [interactive Workbench](https://thegrahamfoundation.github.io/Morse-36/workbench/) for the current research model.

---

**Morse/36 — Compact Machine Intent.**
