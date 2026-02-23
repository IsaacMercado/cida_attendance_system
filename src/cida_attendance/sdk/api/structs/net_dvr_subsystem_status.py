from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SUBSYSTEM_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_SUBSYSTEM_STATUS, [
    ('bySubSystemType', BYTE),
    ('bySubSystemNo', BYTE),
    ('byOnlineStatus', BYTE),
    ('byRes', BYTE * 49),
])

NET_DVR_SUBSYSTEM_STATUS = struct_tagNET_DVR_SUBSYSTEM_STATUS
LPNET_DVR_SUBSYSTEM_STATUS = POINTER(struct_tagNET_DVR_SUBSYSTEM_STATUS)
tagNET_DVR_SUBSYSTEM_STATUS = struct_tagNET_DVR_SUBSYSTEM_STATUS
