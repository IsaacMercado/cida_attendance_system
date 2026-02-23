from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ROOM_CUSTOM_COND(Structure):
    pass

_S(struct_tagNET_DVR_ROOM_CUSTOM_COND, [
    ('dwSize', DWORD),
    ('dwRoomNumber', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_ROOM_CUSTOM_COND = struct_tagNET_DVR_ROOM_CUSTOM_COND
LPNET_DVR_ROOM_CUSTOM_COND = POINTER(struct_tagNET_DVR_ROOM_CUSTOM_COND)
tagNET_DVR_ROOM_CUSTOM_COND = struct_tagNET_DVR_ROOM_CUSTOM_COND
