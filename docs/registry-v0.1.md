# Morse/36 Registry — pre-v0.1

The registry binds **Morse/36 word(s)** to canonical **FTIP semantics**.

## Rule

```text
Morse/36 word(s) ⇄ FTIP semantic intent
```

The registry does not expose source-format field names and does not require the wire to carry route/action/resource tuples.

## Entry shape

A future accepted entry should record:

- canonical Morse word;
- canonical FTIP meaning;
- protocol/registry version;
- intent class and mutation characteristics;
- required arguments or external references, if any;
- authorization considerations;
- deterministic test vectors;
- rationale and compatibility impact.

## Word assignments

**No production word assignments are frozen yet.** Early endpoint/action/resource codes from the tuple-frame experiment are retained only in git history and MUST NOT be interpreted as current Morse/36 wire syntax.

The first registry RFC should define the word alphabet, collision rules, composition rules, reserved namespaces and immutable registry digest format before assigning canonical public words.

## Governance

Published registry releases are immutable. A word MUST NOT silently change FTIP meaning. Any incompatible semantic change requires a new word or registry version and explicit peer negotiation.
