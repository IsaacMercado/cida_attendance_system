from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LAMP_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_LAMP_STATUS, [
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('byLampName', BYTE * 32),
    ('byLampState1', BYTE * 32),
    ('byLampState2', BYTE * 32),
    ('byLampState3', BYTE * 32),
    ('byRes', BYTE * 32),
])

NET_DVR_LAMP_STATUS = struct_tagNET_DVR_LAMP_STATUS
LPNET_DVR_LAMP_STATUS = POINTER(struct_tagNET_DVR_LAMP_STATUS)
tagNET_DVR_LAMP_STATUS = struct_tagNET_DVR_LAMP_STATUS
