import builtins
from _typeshed import Incomplete

import MySQLdb._exceptions

version_info: tuple[Incomplete, ...]

class DataError(MySQLdb._exceptions.DatabaseError): ...
class DatabaseError(MySQLdb._exceptions.Error): ...
class Error(MySQLdb._exceptions.MySQLError): ...
class IntegrityError(MySQLdb._exceptions.DatabaseError): ...
class InterfaceError(MySQLdb._exceptions.Error): ...
class InternalError(MySQLdb._exceptions.DatabaseError): ...
class MySQLError(Exception): ...
class NotSupportedError(MySQLdb._exceptions.DatabaseError): ...
class OperationalError(MySQLdb._exceptions.DatabaseError): ...
class ProgrammingError(MySQLdb._exceptions.DatabaseError): ...
class Warning(builtins.Warning, MySQLdb._exceptions.MySQLError): ...

class connection:
    client_flag: Incomplete
    converter: Incomplete
    open: Incomplete
    port: Incomplete
    server_capabilities: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def _get_native_connection(self): ...
    def affected_rows(self): ...
    def autocommit(self, on): ...
    def change_user(self, *args, **kwargs): ...
    def character_set_name(self): ...
    def close(self): ...
    def commit(self): ...
    def dump_debug_info(self): ...
    def errno(self): ...
    def error(self): ...
    def escape(self, obj, dict): ...
    def escape_string(self, s): ...
    def field_count(self): ...
    def fileno(self): ...
    def get_autocommit(self): ...
    def get_character_set_info(self): ...
    def get_host_info(self): ...
    def get_proto_info(self): ...
    def get_server_info(self): ...
    def info(self): ...
    def insert_id(self): ...
    def kill(self, *args, **kwargs): ...
    def next_result(self): ...
    def ping(self): ...
    def query(self, query): ...
    def read_query_result(self): ...
    def rollback(self): ...
    def select_db(self, *args, **kwargs): ...
    def send_query(self, *args, **kwargs): ...
    def set_character_set(self, charset: str) -> None: ...
    def set_server_option(self, option): ...
    def shutdown(self): ...
    def sqlstate(self): ...
    def stat(self): ...
    def store_result(self): ...
    def string_literal(self, obj, /) -> str: ...
    def thread_id(self): ...
    def use_result(self): ...
    def discard_result(self) -> None: ...
    def warning_count(self): ...
    def __delattr__(self, name: str, /) -> None: ...
    def __setattr__(self, name: str, value, /) -> None: ...

class result:
    converter: Incomplete
    has_next: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def data_seek(self, n): ...
    def describe(self): ...
    def fetch_row(self, *args, **kwargs): ...
    def discard(self) -> None: ...
    def field_flags(self): ...
    def num_fields(self): ...
    def num_rows(self): ...
    def __delattr__(self, name: str, /) -> None: ...
    def __setattr__(self, name: str, value, /) -> None: ...

def connect(*args, **kwargs): ...
def debug(*args, **kwargs): ...
def escape(obj, dict): ...
def escape_string(s): ...
def get_client_info(): ...
def string_literal(obj, /) -> str: ...
