from _thread import LockType, allocate_lock as Lock
from typing import Generic, NewType, TypeVar

__all__ = ["Lock", "Queue", "EmptyTimeout"]

_T = TypeVar("_T")
_Cookie = NewType("_Cookie", LockType)

class EmptyTimeout(Exception): ...

class Queue(Generic[_T]):
    unfinished_tasks: int
    def __init__(self) -> None: ...
    def task_done(self) -> None: ...
    def qsize(self) -> int: ...
    def empty(self) -> bool: ...
    def full(self) -> bool: ...
    def put(self, item: _T) -> None: ...
    def get(self, cookie: _Cookie, timeout: int = -1) -> _T: ...
    def allocate_cookie(self) -> _Cookie: ...
    def kill(self) -> None: ...
