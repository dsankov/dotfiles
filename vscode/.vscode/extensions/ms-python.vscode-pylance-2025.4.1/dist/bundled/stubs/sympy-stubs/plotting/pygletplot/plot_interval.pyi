from typing import Any, Callable, Generator

from sympy.core.numbers import Integer
from sympy.core.symbol import Symbol

class PlotInterval:
    @staticmethod
    def require_all_args(f) -> Callable[..., Any]: ...
    def __init__(self, *args) -> None: ...
    def get_v(self) -> Symbol | None: ...
    def set_v(self, v) -> None: ...
    def get_v_min(self) -> None: ...
    def set_v_min(self, v_min) -> None: ...
    def get_v_max(self) -> None: ...
    def set_v_max(self, v_max) -> None: ...
    def get_v_steps(self) -> Integer | None: ...
    def set_v_steps(self, v_steps) -> None: ...
    @require_all_args
    def get_v_len(self) -> Any: ...

    v = ...
    v_min = ...
    v_max = ...
    v_steps = ...
    v_len = ...
    def fill_from(self, b) -> None: ...
    @staticmethod
    def try_parse(*args) -> PlotInterval | None: ...
    @require_all_args
    def assert_complete(self) -> None: ...
    @require_all_args
    def vrange(self) -> Generator[Any, Any, None]: ...
    @require_all_args
    def vrange2(self) -> Generator[tuple[Any, Any], Any, None]: ...
    def frange(self) -> Generator[float, Any, None]: ...
