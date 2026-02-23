from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PHONE_DOOR_RIGHT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PHONE_DOOR_RIGHT_CFG, [
    ('dwSize', DWORD),
    ('byOpenRight', BYTE * 256),
    ('byCloseRight', BYTE * 256),
    ('byNormalOpenRight', BYTE * 256),
    ('byNormalCloseRight', BYTE * 256),
    ('byArmRight', BYTE * 512),
    ('byDisarmRight', BYTE * 512),
    ('byRes', BYTE * 256),
])

NET_DVR_PHONE_DOOR_RIGHT_CFG = struct_tagNET_DVR_PHONE_DOOR_RIGHT_CFG
LPNET_DVR_PHONE_DOOR_RIGHT_CFG = POINTER(struct_tagNET_DVR_PHONE_DOOR_RIGHT_CFG)
tagNET_DVR_PHONE_DOOR_RIGHT_CFG = struct_tagNET_DVR_PHONE_DOOR_RIGHT_CFG
