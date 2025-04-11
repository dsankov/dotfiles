import sys
from _typeshed import ReadableBuffer
from collections.abc import Mapping
from typing import Any, Literal, overload
from typing_extensions import TypeAlias
from xml.sax import _Source, xmlreader
from xml.sax.handler import _ContentHandlerProtocol

if sys.version_info >= (3, 10):
    from xml.sax.handler import LexicalHandler

_BoolType: TypeAlias = Literal[0, 1] | bool

version: str
AttributesImpl = xmlreader.AttributesImpl
AttributesNSImpl = xmlreader.AttributesNSImpl

class _ClosedParser:
    ErrorColumnNumber: int
    ErrorLineNumber: int

class ExpatLocator(xmlreader.Locator):
    def __init__(self, parser: ExpatParser) -> None: ...
    def getColumnNumber(self) -> int | None: ...
    def getLineNumber(self) -> int: ...
    def getPublicId(self) -> str | None: ...
    def getSystemId(self) -> str | None: ...

class ExpatParser(xmlreader.IncrementalParser, xmlreader.Locator):
    def __init__(self, namespaceHandling: _BoolType = 0, bufsize: int = 65516) -> None: ...
    def parse(self, source: xmlreader.InputSource | _Source) -> None: ...
    def prepareParser(self, source: xmlreader.InputSource) -> None: ...
    def setContentHandler(self, handler: _ContentHandlerProtocol) -> None: ...
    def getFeature(self, name: str) -> _BoolType: ...
    def setFeature(self, name: str, state: _BoolType) -> None: ...
    if sys.version_info >= (3, 10):
        @overload
        def getProperty(self, name: Literal["http://xml.org/sax/properties/lexical-handler"]) -> LexicalHandler | None: ...

    @overload
    def getProperty(self, name: Literal["http://www.python.org/sax/properties/interning-dict"]) -> dict[str, Any] | None: ...
    @overload
    def getProperty(self, name: Literal["http://xml.org/sax/properties/xml-string"]) -> bytes | None: ...
    @overload
    def getProperty(self, name: str) -> object: ...
    if sys.version_info >= (3, 10):
        @overload
        def setProperty(self, name: Literal["http://xml.org/sax/properties/lexical-handler"], value: LexicalHandler) -> None: ...

    @overload
    def setProperty(
        self, name: Literal["http://www.python.org/sax/properties/interning-dict"], value: dict[str, Any]
    ) -> None: ...
    @overload
    def setProperty(self, name: str, value: object) -> None: ...
    if sys.version_info >= (3, 9):
        def feed(self, data: str | ReadableBuffer, isFinal: bool = False) -> None: ...
    else:
        def feed(self, data: str | ReadableBuffer, isFinal: _BoolType = 0) -> None: ...

    def flush(self) -> None: ...
    def close(self) -> None: ...
    def reset(self) -> None: ...
    def getColumnNumber(self) -> int | None: ...
    def getLineNumber(self) -> int: ...
    def getPublicId(self) -> str | None: ...
    def getSystemId(self) -> str | None: ...
    def start_element(self, name: str, attrs: Mapping[str, str]) -> None: ...
    def end_element(self, name: str) -> None: ...
    def start_element_ns(self, name: str, attrs: Mapping[str, str]) -> None: ...
    def end_element_ns(self, name: str) -> None: ...
    def processing_instruction(self, target: str, data: str) -> None: ...
    def character_data(self, data: str) -> None: ...
    def start_namespace_decl(self, prefix: str | None, uri: str) -> None: ...
    def end_namespace_decl(self, prefix: str | None) -> None: ...
    def start_doctype_decl(self, name: str, sysid: str | None, pubid: str | None, has_internal_subset: bool) -> None: ...
    def unparsed_entity_decl(self, name: str, base: str | None, sysid: str, pubid: str | None, notation_name: str) -> None: ...
    def notation_decl(self, name: str, base: str | None, sysid: str, pubid: str | None) -> None: ...
    def external_entity_ref(self, context: str, base: str | None, sysid: str, pubid: str | None) -> int: ...
    def skipped_entity_handler(self, name: str, is_pe: bool) -> None: ...

def create_parser(namespaceHandling: int = 0, bufsize: int = 65516) -> ExpatParser: ...
