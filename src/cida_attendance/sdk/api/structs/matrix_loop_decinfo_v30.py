from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_176 import NET_DVR_MATRIX_CHAN_INFO_V30


class struct_tagMATRIX_LOOP_DECINFO_V30(Structure):
    pass

_S(struct_tagMATRIX_LOOP_DECINFO_V30, [
    ('dwSize', DWORD),
    ('dwPoolTime', DWORD),
    ('struchanConInfo', NET_DVR_MATRIX_CHAN_INFO_V30 * 64),
    ('byRes', BYTE * 16),
])

NET_DVR_MATRIX_LOOP_DECINFO_V30 = struct_tagMATRIX_LOOP_DECINFO_V30
LPNET_DVR_MATRIX_LOOP_DECINFO_V30 = POINTER(struct_tagMATRIX_LOOP_DECINFO_V30)
tagMATRIX_LOOP_DECINFO_V30 = struct_tagMATRIX_LOOP_DECINFO_V30
