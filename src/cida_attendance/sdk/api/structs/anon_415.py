from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_415(Structure):
    pass

_S(struct_anon_415, [
    ('sData', BYTE * 128),
])

NET_DVR_IGNORE_STRING = struct_anon_415
LPNET_DVR_IGNORE_STRING = POINTER(struct_anon_415)
