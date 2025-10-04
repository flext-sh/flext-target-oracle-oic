"""Version information for flext-target-oracle-oic."""

from __future__ import annotations

from typing import Final

# Version components
MAJOR: Final[int] = 0
MINOR: Final[int] = 9
PATCH: Final[int] = 0

# Version string
__version__: Final[str] = f"{MAJOR}.{MINOR}.{PATCH}"
__version_info__: Final[tuple[int, int, int]] = (MAJOR, MINOR, PATCH)


class FlexttargetOracleOicVersion:
    """Version information container for flext-target-oracle-oic."""

    def __init__(self) -> None:
        self.major = MAJOR
        self.minor = MINOR
        self.patch = PATCH
        self.version = __version__
        self.version_info = __version_info__

    @classmethod
    def current(cls) -> FlexttargetOracleOicVersion:
        """Return current version information."""
        return cls()


VERSION: Final[FlexttargetOracleOicVersion] = FlexttargetOracleOicVersion.current()

__all__ = ["VERSION", "FlexttargetOracleOicVersion", "__version__", "__version_info__"]
