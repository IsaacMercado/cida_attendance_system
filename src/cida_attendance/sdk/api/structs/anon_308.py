from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_anon_308(Structure):
    pass

_S(struct_anon_308, [
    ('byPipChan', BYTE),
    ('byRes', BYTE * 3),
    ('wTopLeftX', WORD),
    ('wTopLeftY', WORD),
])

NET_DVR_INQUEST_PIP_PARAM = struct_anon_308
LPNET_DVR_INQUEST_PIP_PARAM = POINTER(struct_anon_308)
