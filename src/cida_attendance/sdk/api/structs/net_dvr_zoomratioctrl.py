from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ZOOMRATIOCTRL(Structure):
    pass

_S(struct_tagNET_DVR_ZOOMRATIOCTRL, [
    ('dwSize', DWORD),
    ('dwChan', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_ZOOMRATIOCTRL = struct_tagNET_DVR_ZOOMRATIOCTRL
LPNET_DVR_ZOOMRATIOCTRL = POINTER(struct_tagNET_DVR_ZOOMRATIOCTRL)
tagNET_DVR_ZOOMRATIOCTRL = struct_tagNET_DVR_ZOOMRATIOCTRL
