import sys
from _typeshed import StrPath
from collections.abc import Iterator, Sequence
from io import TextIOWrapper
from os import PathLike
from typing import IO, Literal, TypeVar, overload
from typing_extensions import Self
from zipfile import ZipFile

_ZF = TypeVar("_ZF", bound=ZipFile)

if sys.version_info >= (3, 12):
    __all__ = ["Path"]

    class InitializedState:
        def __init__(self, *args: object, **kwargs: object) -> None: ...
        def __getstate__(self) -> tuple[list[object], dict[object, object]]: ...
        def __setstate__(self, state: Sequence[tuple[list[object], dict[object, object]]]) -> None: ...

    class CompleteDirs(InitializedState, ZipFile):
        def resolve_dir(self, name: str) -> str: ...
        @overload
        @classmethod
        def make(cls, source: ZipFile) -> CompleteDirs: ...
        @overload
        @classmethod
        def make(cls, source: StrPath | IO[bytes]) -> Self: ...
        if sys.version_info >= (3, 13):
            @classmethod
            def inject(cls, zf: _ZF) -> _ZF: ...

    class Path:
        root: CompleteDirs
        at: str
        def __init__(self, root: ZipFile | StrPath | IO[bytes], at: str = "") -> None: ...
        @property
        def name(self) -> str: ...
        @property
        def parent(self) -> PathLike[str]: ...  # undocumented
        @property
        def filename(self) -> PathLike[str]: ...  # undocumented
        @property
        def suffix(self) -> str: ...
        @property
        def suffixes(self) -> list[str]: ...
        @property
        def stem(self) -> str: ...
        @overload
        def open(
            self,
            mode: Literal["r", "w"] = "r",
            encoding: str | None = None,
            errors: str | None = None,
            newline: str | None = None,
            line_buffering: bool = ...,
            write_through: bool = ...,
            *,
            pwd: bytes | None = None,
        ) -> TextIOWrapper: ...
        @overload
        def open(self, mode: Literal["rb", "wb"], *, pwd: bytes | None = None) -> IO[bytes]: ...
        def iterdir(self) -> Iterator[Self]: ...
        def is_dir(self) -> bool: ...
        def is_file(self) -> bool: ...
        def exists(self) -> bool: ...
        def read_text(
            self,
            encoding: str | None = ...,
            errors: str | None = ...,
            newline: str | None = ...,
            line_buffering: bool = ...,
            write_through: bool = ...,
        ) -> str: ...
        def read_bytes(self) -> bytes: ...
        def joinpath(self, *other: StrPath) -> Path: ...
        def glob(self, pattern: str) -> Iterator[Self]: ...
        def rglob(self, pattern: str) -> Iterator[Self]: ...
        def is_symlink(self) -> Literal[False]: ...
        def relative_to(self, other: Path, *extra: StrPath) -> str: ...
        def match(self, path_pattern: str) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __truediv__(self, add: StrPath) -> Path: ...
