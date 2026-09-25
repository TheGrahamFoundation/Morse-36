# Morse/36 Workbench

A zero-dependency browser experiment for the current Morse/36 layering.

```text
source payload
    ↓
FTIP semantic intent
    ↓
Morse/36 word(s)
```

Paste JSON, YAML, XML, or raw text on the left. The workbench extracts an illustrative FTIP intent and then produces an **experimental deterministic word representation**.

The workbench deliberately does **not** display the old `A>S|D|V|R` or `ASD|VCE|GET|001` tuple style. Those were useful early decomposition sketches, but they are not the intended wire abstraction.

The current browser encoder is non-normative: its generated word is a deterministic research token so the pipeline can be inspected before the public word registry and canonical codec are frozen.

This is not Benchmark 001 and not proof of compression. The benchmark must separately measure source bytes, FTIP normalization cost, word bytes, registry overhead, latency and semantic fidelity.
