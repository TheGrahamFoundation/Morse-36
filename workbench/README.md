# Morse/36 Example Workbench

A zero-dependency browser experiment demonstrating the **Compact Machine Intent** idea.

Open `index.html` locally. Paste JSON, YAML, XML, or raw text on the left. The workbench performs a deliberately small deterministic normalization and maps recognized semantics through an experimental registry into an illustrative Morse/36 frame.

This is **not** the production codec and **not** Benchmark 001. It intentionally shows the transformation so the hypothesis can be inspected:

```text
payload
  ↓
semantic words
  ↓
shared deterministic registry
  ↓
M36 / M366 representation
```

The bundled example maps:

```text
alfred     → A
sophia     → S
diagnostic → D
voice      → V
request    → R
```

and demonstrates:

```text
A>S|D|V|R
```

The UI reports UTF-8 payload bytes and representation bytes only. It does not include transport, registry distribution, schema/version negotiation, compression, or system-level resource cost. Those belong in Benchmark 001.

The point of this workbench is not to prove that Morse/36 wins. It is to make the idea falsifiable and easy to experiment with.
