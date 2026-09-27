# Experimental Codec A — Control Plane

**Status:** Experimental / dogfood  
**Envelope:** M36  
**Maximum:** 36 characters

Codec A is the first running internal implementation of Morse/36. It is used by
David Labs' Git Blend experiment to move compact control-plane intent between
Git Blend, Workbench, Sparks, and publishing adapters.

It is **not** the final public Morse/36 grammar.

## Layout

```text
M36A + III + TTTTTTTT + ARG
```

- `M36A` — self-identifying Morse/36 Codec A header
- `III` — registered three-character intent
- `TTTTTTTT` — deterministic eight-character trace fingerprint
- `ARG` — optional compact argument
- entire packet MUST be <= 36 characters

## Initial registry

| Code | Intent |
| --- | --- |
| `GBL` | Git Blend evaluation request |
| `SPD` | Sparks debit |
| `RFL` | Sparks refuel required/requested |
| `PUB` | Workbench decision: publish |
| `HLD` | Workbench decision: hold |
| `IGN` | Workbench decision: ignore |
| `ACK` | acknowledgement |
| `ERR` | deterministic error |

Example:

```text
M36ASPD7A91B04E5
```

means: an M36 Codec-A packet carrying a Sparks-debit intent, trace
`7A91B04E`, argument `5`.

## Security boundary

Codec A carries **intent only**. It MUST NOT carry card details, access tokens,
Stripe secrets, OAuth credentials, or other payment/authentication secrets.

For the Git Blend dogfood path:

```text
Git → Blend → M36 GBL → Workbench
Workbench → M36 SPD → Sparks
Workbench → M36 PUB/HLD/IGN → publisher
Sparks → M36 RFL → authenticated refuel flow
```

Stripe remains the fiat/payment rail. Morse/36 only tells the system what needs
to happen.
