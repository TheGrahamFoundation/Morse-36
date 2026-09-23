# Morse/36 Registry v0.1

The registry is deliberately small. Codes become normative only after review and a versioned release.

## Message kinds

| Code | Meaning |
|---|---|
| `Q` | Query without intended mutation |
| `C` | Command that may mutate state |
| `E` | Event notification |
| `R` | Response with result reference |
| `A` | Acknowledgement |
| `X` | Error |
| `H` | Session handshake |

## Experimental endpoints

| Code | Agent/service |
|---|---|
| `ALFR` | Alfred |
| `SOPH` | Sophia |
| `HUBL` | Hubble |
| `BLND` | Blend |
| `FABR` | Fabric |
| `FOXX` | Fox control plane |
| `SHOP` | Shop |
| `FFFF` | Broadcast; disabled by default |

## Initial actions

| Code | Meaning | Expected mutation |
|---|---|---|
| `GET` | Retrieve | No |
| `RUN` | Execute registered operation | Maybe |
| `PUT` | Create or replace | Yes |
| `DEL` | Delete | Yes |
| `ACK` | Acknowledge | No |
| `NAK` | Reject | No |
| `SYN` | Synchronize state | Maybe |

## Initial resources

| Code | Meaning |
|---|---|
| `DIAG` | Diagnostic result |
| `DLM0` | Deterministic Language Model manifest |
| `STAT` | Service status |
| `CONF` | Configuration |
| `TASK` | Task record |
| `DATA` | Referenced data |
| `AUTH` | Authentication/session material |

## Initial contexts

| Code | Meaning |
|---|---|
| `GCP0` | Google Cloud default profile |
| `AWS0` | Amazon Web Services default profile |
| `AZR0` | Microsoft Azure default profile |
| `LOC0` | Local runtime |
| `TEST` | Non-production test bed |
| `PROD` | Production; prohibited in v0.1 experiments |

## Governance

Every registry change MUST include a rationale, collision analysis, compatibility impact, and test vector. Published registry releases are immutable. Changes create a new registry digest or version; peers MUST NOT silently reinterpret an existing code.
