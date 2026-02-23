from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MAGNETIC_DOOR_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_MAGNETIC_DOOR_STATUS, [
    ('byMagneticDoorStatus', BYTE),
    ('byRes', BYTE * 255),
])

NET_DVR_MAGNETIC_DOOR_STATUS = struct_tagNET_DVR_MAGNETIC_DOOR_STATUS
LPNET_DVR_MAGNETIC_DOOR_STATUS = POINTER(struct_tagNET_DVR_MAGNETIC_DOOR_STATUS)
tagNET_DVR_MAGNETIC_DOOR_STATUS = struct_tagNET_DVR_MAGNETIC_DOOR_STATUS
