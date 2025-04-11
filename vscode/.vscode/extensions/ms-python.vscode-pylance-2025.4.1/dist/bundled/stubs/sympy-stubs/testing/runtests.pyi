import doctest as pdoctest
from collections import namedtuple
from contextlib import contextmanager
from doctest import DocTestFinder, DocTestRunner
from typing import Any, Generator, Literal

IS_WINDOWS = ...
ON_CI = ...
SPLIT_DENSITY = ...
SPLIT_DENSITY_SLOW = ...

class Skipped(Exception): ...
class TimeOutError(Exception): ...
class DependencyError(Exception): ...

def convert_to_native_paths(lst) -> list[Any]: ...
def get_sympy_dir() -> str: ...
def setup_pprint() -> bool: ...
@contextmanager
def raise_on_deprecated() -> Generator[None, Any, None]: ...
def run_in_subprocess_with_hash_randomization(
    function, function_args=..., function_kwargs=..., command=..., module=..., force=...
) -> int | Any | Literal[False]: ...
def run_all_tests(
    test_args=..., test_kwargs=..., doctest_args=..., doctest_kwargs=..., examples_args=..., examples_kwargs=...
) -> None: ...
def test(*paths, subprocess=..., rerun=..., **kwargs) -> bool | None: ...
def doctest(*paths, subprocess=..., rerun=..., **kwargs) -> bool | None: ...

sp = ...

def split_list(l, split, density=...): ...

SymPyTestResults = namedtuple("SymPyTestResults", "failed attempted")

def sympytestfile(
    filename,
    module_relative=...,
    name=...,
    package=...,
    globs=...,
    verbose=...,
    report=...,
    optionflags=...,
    extraglobs=...,
    raise_on_error=...,
    parser=...,
    encoding=...,
) -> SymPyTestResults: ...

class SymPyTests:
    def __init__(self, reporter, kw=..., post_mortem=..., seed=..., fast_threshold=..., slow_threshold=...) -> None: ...
    def test(self, sort=..., timeout=..., slow=..., enhance_asserts=..., fail_on_timeout=...): ...
    def test_file(self, filename, sort=..., timeout=..., slow=..., enhance_asserts=..., fail_on_timeout=...): ...
    def matches(self, x) -> bool: ...
    def get_test_files(self, dir, pat=...) -> list[Any]: ...

class SymPyDocTests:
    def __init__(self, reporter, normal) -> None: ...
    def test(self): ...
    def test_file(self, filename) -> None: ...
    def get_test_files(self, dir, pat=..., init_only=...) -> list[Any]: ...

class SymPyDocTestFinder(DocTestFinder): ...

class SymPyDocTestRunner(DocTestRunner):
    def run(self, test, compileflags=..., out=..., clear_globs=...): ...

monkeypatched_methods = ...

class SymPyOutputChecker(pdoctest.OutputChecker):
    def __init__(self) -> None: ...
    def check_output(self, want, got, optionflags) -> bool: ...

class Reporter: ...

class PyTestReporter(Reporter):
    def __init__(self, verbose=..., tb=..., colors=..., force_colors=..., split=...) -> None: ...
    def root_dir(self, dir) -> None: ...
    @property
    def terminal_width(self) -> Any | int: ...
    def write(self, text, color=..., align=..., width=..., force_colors=...) -> None: ...
    def write_center(self, text, delim=...) -> None: ...
    def write_exception(self, e, val, tb) -> None: ...
    def start(self, seed=..., msg=...) -> None: ...
    def finish(self) -> bool: ...
    def entering_filename(self, filename, n) -> None: ...
    def leaving_filename(self) -> None: ...
    def entering_test(self, f) -> None: ...
    def test_xfail(self) -> None: ...
    def test_xpass(self, v) -> None: ...
    def test_fail(self, exc_info) -> None: ...
    def doctest_fail(self, name, error_msg) -> None: ...
    def test_pass(self, char=...) -> None: ...
    def test_skip(self, v=...) -> None: ...
    def test_exception(self, exc_info) -> None: ...
    def import_error(self, filename, exc_info) -> None: ...
