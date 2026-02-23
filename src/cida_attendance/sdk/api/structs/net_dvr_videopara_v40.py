from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VIDEOPARA_V40(Structure):
    pass

_S(struct_tagNET_DVR_VIDEOPARA_V40, [
    ('dwChannel', DWORD),
    ('dwVideoParamType', DWORD),
    ('dwVideoParamValue', DWORD),
    ('byRes', BYTE * 12),
])

NET_DVR_VIDEOPARA_V40 = struct_tagNET_DVR_VIDEOPARA_V40
LPNET_DVR_VIDEOPARA_V40 = POINTER(struct_tagNET_DVR_VIDEOPARA_V40)
tagNET_DVR_VIDEOPARA_V40 = struct_tagNET_DVR_VIDEOPARA_V40
