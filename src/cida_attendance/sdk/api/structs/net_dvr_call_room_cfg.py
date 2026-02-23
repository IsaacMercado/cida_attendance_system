from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, SHORT, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CALL_ROOM_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CALL_ROOM_CFG, [
    ('dwSize', DWORD),
    ('nFloorNumber', SHORT),
    ('wRoomNumber', WORD),
    ('byManageCenter', BYTE),
    ('byRes1', BYTE * 3),
    ('byCalledName', BYTE * 64),
    ('byRes', BYTE * 60),
])

NET_DVR_CALL_ROOM_CFG = struct_tagNET_DVR_CALL_ROOM_CFG
LPNET_DVR_CALL_ROOM_CFG = POINTER(struct_tagNET_DVR_CALL_ROOM_CFG)
tagNET_DVR_CALL_ROOM_CFG = struct_tagNET_DVR_CALL_ROOM_CFG
