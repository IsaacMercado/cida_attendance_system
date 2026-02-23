from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RING_UPLOAD_CFG(Structure):
    pass

_S(struct_tagNET_DVR_RING_UPLOAD_CFG, [
    ('dwSize', DWORD),
    ('dwRingID', DWORD),
    ('byRingName', BYTE * 128),
    ('dwRingSize', DWORD),
    ('byRingType', BYTE),
    ('byRes', BYTE * 363),
])

NET_DVR_RING_UPLOAD_CFG = struct_tagNET_DVR_RING_UPLOAD_CFG
LPNET_DVR_RING_UPLOAD_CFG = POINTER(struct_tagNET_DVR_RING_UPLOAD_CFG)
tagNET_DVR_RING_UPLOAD_CFG = struct_tagNET_DVR_RING_UPLOAD_CFG
