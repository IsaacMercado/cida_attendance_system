from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_297(Structure):
    pass

_S(struct_anon_297, [
    ('byItemOrder', BYTE * 15),
    ('byDelimiter', BYTE),
])

NET_DVR_PICTURE_NAME = struct_anon_297
LPNET_DVR_PICTURE_NAME = POINTER(struct_anon_297)
