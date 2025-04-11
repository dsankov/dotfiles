import sys
import types
from _typeshed import Incomplete, ReadableBuffer, WriteableBuffer
from collections.abc import Callable, Hashable
from typing import Any, ClassVar, Literal, Protocol, SupportsIndex, TypeVar, final, overload
from typing_extensions import TypeAlias

_T = TypeVar("_T")

class _Allocator(Protocol):
    def __call__(self, cdecl: str | CType, init: Any = ...) -> _CDataBase: ...

__version__: str

FFI_CDECL: int
FFI_DEFAULT_ABI: int
RTLD_GLOBAL: int
RTLD_LAZY: int
RTLD_LOCAL: int
RTLD_NOW: int
if sys.platform == "linux":
    RTLD_DEEPBIND: int
if sys.platform != "win32":
    RTLD_NODELETE: int
    RTLD_NOLOAD: int

@final
class CField:
    bitshift: Incomplete
    bitsize: Incomplete
    flags: Incomplete
    offset: Incomplete
    type: Incomplete

@final
class CLibrary:
    def close_lib(self) -> None: ...
    def load_function(self, *args, **kwargs): ...
    def read_variable(self, *args, **kwargs): ...
    def write_variable(self, *args, **kwargs): ...

@final
class CType:
    abi: Incomplete
    args: Incomplete
    cname: Incomplete
    elements: Incomplete
    ellipsis: Incomplete
    fields: Incomplete
    item: Incomplete
    kind: Incomplete
    length: Incomplete
    relements: Incomplete
    result: Incomplete
    def __dir__(self): ...

@final
class Lib:
    def __dir__(self): ...

@final
class _CDataBase:
    __name__: ClassVar[str]
    def __add__(self, other): ...
    def __bool__(self) -> bool: ...
    def __call__(self, *args, **kwargs): ...
    def __complex__(self) -> complex: ...
    def __delitem__(self, other) -> None: ...
    def __dir__(self): ...
    def __enter__(self): ...
    def __eq__(self, other): ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None): ...
    def __float__(self) -> float: ...
    def __ge__(self, other): ...
    def __getitem__(self, index: SupportsIndex | slice): ...
    def __gt__(self, other): ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __iter__(self): ...
    def __le__(self, other): ...
    def __len__(self) -> int: ...
    def __lt__(self, other): ...
    def __ne__(self, other): ...
    def __radd__(self, other): ...
    def __rsub__(self, other): ...
    def __setitem__(self, index: SupportsIndex | slice, object) -> None: ...
    def __sub__(self, other): ...

@final
class buffer:
    __hash__: ClassVar[None]  # type: ignore[assignment]
    def __init__(self, *args, **kwargs) -> None: ...
    def __delitem__(self, other) -> None: ...
    def __eq__(self, other): ...
    def __ge__(self, other): ...
    def __getitem__(self, index): ...
    def __gt__(self, other): ...
    def __le__(self, other): ...
    def __len__(self) -> int: ...
    def __lt__(self, other): ...
    def __ne__(self, other): ...
    def __setitem__(self, index, object) -> None: ...

# These aliases are to work around pyright complaints.
# Pyright doesn't like it when a class object is defined as an alias
# of a global object with the same name.
_tmp_CType = CType
_tmp_buffer = buffer

class FFI:
    CData: TypeAlias = _CDataBase
    CType: TypeAlias = _tmp_CType
    buffer: TypeAlias = _tmp_buffer  # noqa: Y042

    class error(Exception): ...
    NULL: ClassVar[CData]
    RTLD_GLOBAL: ClassVar[int]
    RTLD_LAZY: ClassVar[int]
    RTLD_LOCAL: ClassVar[int]
    RTLD_NOW: ClassVar[int]
    if sys.platform != "win32":
        RTLD_DEEPBIND: ClassVar[int]
        RTLD_NODELETE: ClassVar[int]
        RTLD_NOLOAD: ClassVar[int]

    errno: int

    def __init__(
        self,
        module_name: bytes = ...,
        _version: int = ...,
        _types: bytes = ...,
        _globals: tuple[bytes | int, ...] = ...,
        _struct_unions: tuple[tuple[bytes, ...], ...] = ...,
        _enums: tuple[bytes, ...] = ...,
        _typenames: tuple[bytes, ...] = ...,
        _includes: tuple[FFI, ...] = ...,
    ) -> None: ...
    @overload
    def addressof(self, cdata: CData, /, *field_or_index: str | int) -> CData: ...
    @overload
    def addressof(self, library: Lib, name: str, /) -> CData: ...
    def alignof(self, cdecl: str | CType | CData, /) -> int: ...
    @overload
    def callback(
        self,
        cdecl: str | CType,
        python_callable: None = ...,
        error: Any = ...,
        onerror: Callable[[Exception, Any, Any], None] | None = ...,
    ) -> Callable[[Callable[..., _T]], Callable[..., _T]]: ...
    @overload
    def callback(
        self,
        cdecl: str | CType,
        python_callable: Callable[..., _T],
        error: Any = ...,
        onerror: Callable[[Exception, Any, Any], None] | None = ...,
    ) -> Callable[..., _T]: ...
    def cast(self, cdecl: str | CType, value: CData) -> CData: ...
    def def_extern(
        self, name: str = ..., error: Any = ..., onerror: Callable[[Exception, Any, types.TracebackType], Any] = ...
    ) -> Callable[[Callable[..., _T]], Callable[..., _T]]: ...
    def dlclose(self, lib: Lib, /) -> None: ...
    if sys.platform == "win32":
        def dlopen(self, libpath: str | CData, flags: int = ..., /) -> Lib: ...
    else:
        def dlopen(self, libpath: str | CData | None = ..., flags: int = ..., /) -> Lib: ...

    @overload
    def from_buffer(self, cdecl: ReadableBuffer, require_writable: Literal[False] = ...) -> CData: ...
    @overload
    def from_buffer(self, cdecl: WriteableBuffer, require_writable: Literal[True]) -> CData: ...
    @overload
    def from_buffer(self, cdecl: str | CType, python_buffer: ReadableBuffer, require_writable: Literal[False] = ...) -> CData: ...
    @overload
    def from_buffer(self, cdecl: str | CType, python_buffer: WriteableBuffer, require_writable: Literal[True]) -> CData: ...
    def from_handle(self, x: CData, /) -> Any: ...
    @overload
    def gc(self, cdata: CData, destructor: Callable[[CData], Any], size: int = ...) -> CData: ...
    @overload
    def gc(self, cdata: CData, destructor: None, size: int = ...) -> None: ...
    def getctype(self, cdecl: str | CType, replace_with: str = ...) -> str: ...
    if sys.platform == "win32":
        def getwinerror(self, code: int = ...) -> tuple[int, str]: ...

    def init_once(self, func: Callable[[], Any], tag: Hashable) -> Any: ...
    def integer_const(self, name: str) -> int: ...
    def list_types(self) -> tuple[list[str], list[str], list[str]]: ...
    def memmove(self, dest: CData | WriteableBuffer, src: CData | ReadableBuffer, n: int) -> None: ...
    def new(self, cdecl: str | CType, init: Any = ...) -> CData: ...
    @overload
    def new_allocator(self, alloc: None = ..., free: None = ..., should_clear_after_alloc: bool = ...) -> _Allocator: ...
    @overload
    def new_allocator(
        self, alloc: Callable[[int], CData], free: None = ..., should_clear_after_alloc: bool = ...
    ) -> _Allocator: ...
    @overload
    def new_allocator(
        self, alloc: Callable[[int], CData], free: Callable[[CData], Any], should_clear_after_alloc: bool = ...
    ) -> _Allocator: ...
    def new_handle(self, x: Any, /) -> CData: ...
    def offsetof(self, cdecl: str | CType, field_or_index: str | int, /, *__fields_or_indexes: str | int) -> int: ...
    def release(self, cdata: CData, /) -> None: ...
    def sizeof(self, cdecl: str | CType | CData, /) -> int: ...
    def string(self, cdata: CData, maxlen: int = -1) -> bytes | str: ...
    def typeof(self, cdecl: str | CData, /) -> CType: ...
    def unpack(self, cdata: CData, length: int) -> bytes | str | list[Any]: ...

def alignof(cdecl: CType, /) -> int: ...
def callback(
    cdecl: CType,
    python_callable: Callable[..., _T],
    error: Any = ...,
    onerror: Callable[[Exception, Any, Any], None] | None = ...,
    /,
) -> Callable[..., _T]: ...
def cast(cdecl: CType, value: _CDataBase, /) -> _CDataBase: ...
def complete_struct_or_union(
    cdecl: CType,
    fields: list[tuple[str, CType, int, int]],
    ignored: Any,
    total_size: int,
    total_alignment: int,
    sflags: int,
    pack: int,
    /,
) -> None: ...
@overload
def from_buffer(cdecl: CType, python_buffer: ReadableBuffer, /, require_writable: Literal[False] = ...) -> _CDataBase: ...
@overload
def from_buffer(cdecl: CType, python_buffer: WriteableBuffer, /, require_writable: Literal[True]) -> _CDataBase: ...
def from_handle(x: _CDataBase, /) -> Any: ...
@overload
def gcp(cdata: _CDataBase, destructor: Callable[[_CDataBase], Any], size: int = ...) -> _CDataBase: ...
@overload
def gcp(cdata: _CDataBase, destructor: None, size: int = ...) -> None: ...
def get_errno() -> int: ...
def getcname(cdecl: CType, replace_with: str, /) -> str: ...

if sys.platform == "win32":
    def getwinerror(code: int = ...) -> tuple[int, str]: ...

if sys.platform == "win32":
    def load_library(libpath: str | _CDataBase, flags: int = ..., /) -> CLibrary: ...

else:
    def load_library(libpath: str | _CDataBase | None = ..., flags: int = ..., /) -> CLibrary: ...

def memmove(dest: _CDataBase | WriteableBuffer, src: _CDataBase | ReadableBuffer, n: int) -> None: ...
def new_array_type(cdecl: CType, length: int | None, /) -> CType: ...
def new_enum_type(name: str, enumerators: tuple[str, ...], enumvalues: tuple[Any, ...], basetype: CType, /) -> CType: ...
def new_function_type(args: tuple[CType, ...], result: CType, ellipsis: int, abi: int, /) -> CType: ...
def new_pointer_type(cdecl: CType, /) -> CType: ...
def new_primitive_type(name: str, /) -> CType: ...
def new_struct_type(name: str, /) -> CType: ...
def new_union_type(name: str, /) -> CType: ...
def new_void_type() -> CType: ...
def newp(cdecl: CType, init: Any = ..., /) -> _CDataBase: ...
def newp_handle(cdecl: CType, x: Any, /) -> _CDataBase: ...
def rawaddressof(cdecl: CType, cdata: _CDataBase, offset: int, /) -> _CDataBase: ...
def release(cdata: _CDataBase, /) -> None: ...
def set_errno(errno: int, /) -> None: ...
def sizeof(cdecl: CType | _CDataBase, /) -> int: ...
def string(cdata: _CDataBase, maxlen: int) -> bytes | str: ...
def typeof(cdata: _CDataBase, /) -> CType: ...
def typeoffsetof(cdecl: CType, fieldname: str | int, following: bool = ..., /) -> tuple[CType, int]: ...
def unpack(cdata: _CDataBase, length: int) -> bytes | str | list[Any]: ...
