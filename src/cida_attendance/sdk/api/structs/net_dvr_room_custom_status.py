from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ROOM_CUSTOM_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_ROOM_CUSTOM_STATUS, [
    ('dwSize', DWORD),
    ('dwFormerRoomNo', DWORD),
    ('byStatus', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_ROOM_CUSTOM_STATUS = struct_tagNET_DVR_ROOM_CUSTOM_STATUS
LPNET_DVR_ROOM_CUSTOM_STATUS = POINTER(struct_tagNET_DVR_ROOM_CUSTOM_STATUS)
tagNET_DVR_ROOM_CUSTOM_STATUS = struct_tagNET_DVR_ROOM_CUSTOM_STATUS
