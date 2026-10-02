"""Deterministic Morse/36 failure types."""


class Morse36Error(ValueError):
    """Base class for all public Morse/36 errors."""


class RegistryError(Morse36Error):
    """Base class for invalid registries."""


class RegistrySchemaError(RegistryError):
    """The registry does not conform to the supported schema."""


class RegistryDigestError(RegistryError):
    """The registry digest does not match its canonical content."""


class EncodeError(Morse36Error):
    """Base class for encoding failures."""


class UnknownEntryError(EncodeError):
    """No registry entry has the requested name."""


class PacketTooLargeError(EncodeError):
    """The encoded packet exceeds the registry envelope."""


class DecodeError(Morse36Error):
    """Base class for decoding failures."""


class MalformedPacketError(DecodeError):
    """The packet does not follow the selected registry profile."""


class UnknownCodeError(DecodeError):
    """The packet code is not present in the selected registry."""
