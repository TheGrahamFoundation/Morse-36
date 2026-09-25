# Contributing to Morse/36

Morse/36 is currently a **discussion-first research protocol**.

You do not need to arrive with code.

## Start with an idea

Useful contributions include:

- challenging the Compact Machine Intent model;
- proposing real machine-to-machine use cases;
- identifying cases where Morse cannot safely replace representation;
- protocol and registry design;
- healthcare, IoT, robotics, agent, edge, and infrastructure examples;
- security and interoperability criticism;
- benchmark design;
- independent implementations.

Please use **GitHub Discussions** for design conversations when Discussions are enabled on the repository. Issues can be used for concrete, bounded work.

## Code contributors

Code is welcome as the specification matures.

Pull requests should:

1. explain the machine-intent problem being addressed;
2. preserve deterministic semantics;
3. include tests for protocol behavior;
4. avoid claims of efficiency without measurements;
5. avoid introducing a dependency on proprietary Foundation or David Labs infrastructure.

## Merge governance

Pull requests are reviewed before entering the protocol.

Automation and DLM-assisted review may be used to classify changes, run conformance checks, summarize risks, and recommend a disposition. **A model recommendation is not protocol consensus.**

Until governance is explicitly changed, automated systems must not silently redefine public Morse semantics.

Maintainers retain responsibility for accepted changes.

## Conduct

Criticism of the protocol is welcome. Attack the assumption, benchmark, grammar, implementation, or evidence, not the person making the contribution.

The goal is to discover whether Compact Machine Intent works.
