from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ROOM_CUSTOM_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ROOM_CUSTOM_CFG, [
    ('dwSize', DWORD),
    ('dwFormerRoomNo', DWORD),
    ('dwCustomRoomNo', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_ROOM_CUSTOM_CFG = struct_tagNET_DVR_ROOM_CUSTOM_CFG
LPNET_DVR_ROOM_CUSTOM_CFG = POINTER(struct_tagNET_DVR_ROOM_CUSTOM_CFG)
tagNET_DVR_ROOM_CUSTOM_CFG = struct_tagNET_DVR_ROOM_CUSTOM_CFG
