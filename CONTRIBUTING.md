# Contributing to Morse/36

Morse/36 is open research. Criticism, failed experiments, alternative layouts, codecs, threat models, and reproducible measurements are welcome.

## Workflow

1. Open an issue stating the research question or defect.
2. Keep protocol changes separate from implementation changes.
3. Add or update canonical test vectors for semantic changes.
4. Include compatibility and security consequences.
5. Submit a pull request for public review.

## Decision standard

Claims require evidence. Popularity, affiliation, and confidence are not protocol arguments. Negative results remain part of the research record.

## Merge control

No pull request is merged automatically. Merging requires repository checks and explicit approval from the project maintainer.

## Scope guardrail

The v0.1 test bed is limited to synthetic, read-only, non-production operations. Do not connect experimental code to safety-critical or production systems.
