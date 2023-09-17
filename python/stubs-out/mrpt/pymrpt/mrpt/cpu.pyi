from typing import ClassVar

from typing import overload

class feature:
    __doc__: ClassVar[str] = ...  # read-only
    __members__: ClassVar[dict] = ...  # read-only
    AVX: ClassVar[feature] = ...
    AVX2: ClassVar[feature] = ...
    FEATURE_COUNT: ClassVar[feature] = ...
    MMX: ClassVar[feature] = ...
    POPCNT: ClassVar[feature] = ...
    SSE: ClassVar[feature] = ...
    SSE2: ClassVar[feature] = ...
    SSE3: ClassVar[feature] = ...
    SSE4_1: ClassVar[feature] = ...
    SSE4_2: ClassVar[feature] = ...
    SSSE3: ClassVar[feature] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

def features_as_string() -> str: ...
@overload
def overrideDetectedFeature(f: feature, newValue: bool) -> None: ...
@overload
def overrideDetectedFeature(enummrpt, bool) -> void: ...
@overload
def supports(f: feature) -> bool: ...
@overload
def supports(enummrpt) -> bool: ...