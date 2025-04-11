import datetime
from _operator import _SupportsComparison
from _typeshed import Incomplete, SupportsKeysAndGetItem
from collections.abc import Callable, Iterable, Mapping
from logging import Logger
from typing import ClassVar, TypeVar, overload, type_check_only
from typing_extensions import Self

_RangeMapKT = TypeVar("_RangeMapKT", bound=_SupportsComparison)

_T = TypeVar("_T")
_VT = TypeVar("_VT")

log: Logger

class _SimpleStruct:
    def __init__(self, *args, **kw) -> None: ...
    def field_names(self) -> list[str]: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class SYSTEMTIME(_SimpleStruct): ...
class TIME_ZONE_INFORMATION(_SimpleStruct): ...
class DYNAMIC_TIME_ZONE_INFORMATION(_SimpleStruct): ...

class TimeZoneDefinition(DYNAMIC_TIME_ZONE_INFORMATION):
    def __init__(self, *args, **kwargs) -> None: ...
    # TIME_ZONE_INFORMATION fields as obtained by __getattribute__
    bias: datetime.timedelta
    standard_name: str
    standard_start: SYSTEMTIME
    standard_bias: datetime.timedelta
    daylight_name: str
    daylight_start: SYSTEMTIME
    daylight_bias: datetime.timedelta
    def __getattribute__(self, attr: str): ...
    @classmethod
    def current(cls) -> tuple[int, Self]: ...
    def set(self) -> None: ...
    def copy(self) -> Self: ...
    def locate_daylight_start(self, year) -> datetime.datetime: ...
    def locate_standard_start(self, year) -> datetime.datetime: ...

class TimeZoneInfo(datetime.tzinfo):
    tzRegKey: ClassVar[str]
    timeZoneName: str
    fixedStandardTime: bool
    def __init__(self, param: str | TimeZoneDefinition, fix_standard_time: bool = False) -> None: ...
    @overload  # type: ignore[override] # Split definition into overrides
    def tzname(self, dt: datetime.datetime) -> str: ...
    @overload
    def tzname(self, dt: None) -> None: ...
    def getWinInfo(self, targetYear: int) -> TimeZoneDefinition: ...
    @overload  # type: ignore[override] # False-positive, our overload covers all base types
    def utcoffset(self, dt: None) -> None: ...
    @overload
    def utcoffset(self, dt: datetime.datetime) -> datetime.timedelta: ...
    @overload  # type: ignore[override] # False-positive, our overload covers all base types
    def dst(self, dt: None) -> None: ...
    @overload
    def dst(self, dt: datetime.datetime) -> datetime.timedelta: ...
    def GetDSTStartTime(self, year: int) -> datetime.datetime: ...
    def GetDSTEndTime(self, year: int) -> datetime.datetime: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @classmethod
    def local(cls) -> Self: ...
    @classmethod
    def utc(cls) -> Self: ...
    @staticmethod
    def get_sorted_time_zone_names() -> list[str]: ...
    @staticmethod
    def get_all_time_zones() -> list[TimeZoneInfo]: ...
    @staticmethod
    def get_sorted_time_zones(key: Incomplete | None = ...): ...

def utcnow() -> datetime.datetime: ...
def now() -> datetime.datetime: ...
def GetTZCapabilities() -> dict[str, bool]: ...

class DLLHandleCache:
    def __getitem__(self, filename: str) -> int: ...

DLLCache: DLLHandleCache

def resolveMUITimeZone(spec: str) -> str | None: ...

class RangeMap(dict[_RangeMapKT, _VT]):
    sort_params: Mapping[str, Incomplete]
    match: Callable[[_RangeMapKT, _RangeMapKT], bool]
    def __init__(
        self,
        source: SupportsKeysAndGetItem[_RangeMapKT, _VT] | Iterable[tuple[_RangeMapKT, _VT]],
        sort_params: Mapping[str, Incomplete] = {},
        key_match_comparator: Callable[[_RangeMapKT, _RangeMapKT], bool] = ...,
    ) -> None: ...
    @classmethod
    def left(cls, source: SupportsKeysAndGetItem[_RangeMapKT, _VT] | Iterable[tuple[_RangeMapKT, _VT]]) -> Self: ...
    def __getitem__(self, item: _RangeMapKT) -> _VT: ...
    @overload  # type: ignore[override] # Signature simplified over dict and Mapping
    def get(self, key: _RangeMapKT, default: _T) -> _VT | _T: ...
    @overload
    def get(self, key: _RangeMapKT, default: None = None) -> _VT | None: ...
    def bounds(self) -> tuple[_RangeMapKT, _RangeMapKT]: ...
    @type_check_only
    class RangeValueUndefined: ...

    undefined_value: RangeValueUndefined

    class Item(int): ...
    first_item: Item
    last_item: Item
