from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_310(Structure):
    pass

_S(struct_anon_310, [
    ('sSecretKey', BYTE * 16),
    ('byRes', BYTE * 64),
])

NET_DVR_INQUEST_SECRET_INFO = struct_anon_310
LPNET_DVR_INQUEST_SECRET_INFO = POINTER(struct_anon_310)
