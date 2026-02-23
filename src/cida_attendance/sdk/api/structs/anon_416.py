from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_412 import NET_DVR_GENERIC_START
from .anon_413 import NET_DVR_GENERIC_END
from .anon_414 import NET_DVR_GENERIC_DATA_CFG
from .anon_415 import NET_DVR_IGNORE_STRING


class struct_anon_416(Structure):
    pass

_S(struct_anon_416, [
    ('byCaseSensitive', BYTE),
    ('byRes1', BYTE * 7),
    ('struTransactionStart', NET_DVR_GENERIC_START),
    ('struTransactionEnd', NET_DVR_GENERIC_END),
    ('struLineDeli', NET_DVR_GENERIC_DATA_CFG),
    ('struIgnoreString', NET_DVR_IGNORE_STRING * 4),
    ('byRes', BYTE * 40),
])

NET_DVR_POS_GENERIC = struct_anon_416
LPNET_DVR_GENERIC = POINTER(struct_anon_416)
