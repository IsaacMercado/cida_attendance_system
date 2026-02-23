from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RING_SEARCH_CFG(Structure):
    pass

_S(struct_tagNET_DVR_RING_SEARCH_CFG, [
    ('dwSize', DWORD),
    ('dwRingID', DWORD),
    ('byRingName', BYTE * 128),
    ('dwRingSize', DWORD),
    ('byRingType', BYTE),
    ('byRes', BYTE * 303),
])

NET_DVR_RING_SEARCH_CFG = struct_tagNET_DVR_RING_SEARCH_CFG
LPNET_DVR_RING_SEARCH_CFG = POINTER(struct_tagNET_DVR_RING_SEARCH_CFG)
tagNET_DVR_RING_SEARCH_CFG = struct_tagNET_DVR_RING_SEARCH_CFG
