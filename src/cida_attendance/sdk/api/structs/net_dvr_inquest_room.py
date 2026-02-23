from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INQUEST_ROOM(Structure):
    pass

_S(struct_tagNET_DVR_INQUEST_ROOM, [
    ('byRoomIndex', BYTE),
    ('byFileType', BYTE),
    ('byMode', BYTE),
    ('byQuick', BYTE),
    ('byRes', BYTE * 20),
])

NET_DVR_INQUEST_ROOM = struct_tagNET_DVR_INQUEST_ROOM
LPNET_DVR_INQUEST_ROOM = POINTER(struct_tagNET_DVR_INQUEST_ROOM)
tagNET_DVR_INQUEST_ROOM = struct_tagNET_DVR_INQUEST_ROOM
