from _typeshed import Incomplete

class JsonWebToken:
    SENSITIVE_NAMES: Incomplete
    SENSITIVE_VALUES: Incomplete
    def __init__(self, algorithms, private_headers: Incomplete | None = None) -> None: ...
    def check_sensitive_data(self, payload) -> None: ...
    def encode(self, header, payload, key, check: bool = True): ...
    def decode(
        self,
        s,
        key,
        claims_cls: Incomplete | None = None,
        claims_options: Incomplete | None = None,
        claims_params: Incomplete | None = None,
    ): ...

def decode_payload(bytes_payload): ...
def prepare_raw_key(raw): ...
def find_encode_key(key, header): ...
def create_load_key(key): ...
