from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RING_SEARCH_COND(Structure):
    pass

_S(struct_tagNET_DVR_RING_SEARCH_COND, [
    ('dwSize', DWORD),
    ('dwRingID', DWORD),
    ('byRes', BYTE * 300),
])

NET_DVR_RING_SEARCH_COND = struct_tagNET_DVR_RING_SEARCH_COND
LPNET_DVR_RING_SEARCH_COND = POINTER(struct_tagNET_DVR_RING_SEARCH_COND)
tagNET_DVR_RING_SEARCH_COND = struct_tagNET_DVR_RING_SEARCH_COND
