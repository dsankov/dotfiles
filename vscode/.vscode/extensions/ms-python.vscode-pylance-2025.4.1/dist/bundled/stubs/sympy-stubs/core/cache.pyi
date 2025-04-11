from typing import Callable

class _cache(list):
    def print_cache(self) -> None: ...
    def clear_cache(self) -> None: ...

CACHE = ...
print_cache = ...
clear_cache = ...
USE_CACHE = ...
scs = ...
SYMPY_CACHE_SIZE = ...
cacheit = ...

def cached_property(func) -> property: ...
def lazy_function(module: str, name: str) -> Callable:
    class LazyFunctionMeta(type): ...
    class LazyFunction(metaclass=LazyFunctionMeta): ...
