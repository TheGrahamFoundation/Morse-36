"""Experimental Morse/36 Codec A reference implementation.

Codec A is dogfood for the Blend → Workbench → Sparks → publisher control plane.
It is not the final public Morse/36 wire grammar.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass

HEADER = "M36A"
MAX_PACKET = 36
_ARG_RE = re.compile(r"[^A-Z0-9._:-]+")

INTENTS = {
    "GIT_BLEND": "GBL",
    "SPARKS_DEBIT": "SPD",
    "REFUEL": "RFL",
    "PUBLISH": "PUB",
    "HOLD": "HLD",
    "IGNORE": "IGN",
    "ACK": "ACK",
    "ERROR": "ERR",
}
CODES = {code: intent for intent, code in INTENTS.items()}


@dataclass(frozen=True)
class Packet:
    intent: str
    trace: str
    arg: str
    raw: str


def _trace(value: str) -> str:
    return hashlib.blake2s(value.encode("utf-8"), digest_size=4).hexdigest().upper()


def encode(intent: str, trace_id: str, arg: str = "") -> str:
    try:
        code = INTENTS[intent]
    except KeyError as exc:
        raise ValueError(f"unknown intent: {intent}") from exc

    safe_arg = _ARG_RE.sub("", arg.upper())[:21]
    packet = f"{HEADER}{code}{_trace(trace_id)}{safe_arg}"
    if len(packet) > MAX_PACKET:
        raise ValueError("packet exceeds M36 envelope")
    return packet


def decode(packet: str) -> Packet:
    if not packet.startswith(HEADER) or not 15 <= len(packet) <= MAX_PACKET:
        raise ValueError("invalid M36A packet")
    code = packet[4:7]
    intent = CODES.get(code)
    if intent is None:
        raise ValueError(f"unknown intent code: {code}")
    return Packet(
        intent=intent,
        trace=packet[7:15],
        arg=packet[15:],
        raw=packet,
    )
