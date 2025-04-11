import codecs
import re
from _typeshed import ReadableBuffer

dots: re.Pattern[str]
ace_prefix: bytes
sace_prefix: str

def nameprep(label: str) -> str: ...
def ToASCII(label: str) -> bytes: ...
def ToUnicode(label: bytes | str) -> str: ...

class Codec(codecs.Codec):
    def encode(self, input: str, errors: str = "strict") -> tuple[bytes, int]: ...
    def decode(self, input: ReadableBuffer | str, errors: str = "strict") -> tuple[str, int]: ...

class IncrementalEncoder(codecs.BufferedIncrementalEncoder):
    def _buffer_encode(self, input: str, errors: str, final: bool) -> tuple[bytes, int]: ...

class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    def _buffer_decode(self, input: ReadableBuffer | str, errors: str, final: bool) -> tuple[str, int]: ...

class StreamWriter(Codec, codecs.StreamWriter): ...
class StreamReader(Codec, codecs.StreamReader): ...

def getregentry() -> codecs.CodecInfo: ...
