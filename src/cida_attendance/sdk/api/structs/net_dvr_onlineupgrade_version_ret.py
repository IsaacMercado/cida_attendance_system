from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ONLINEUPGRADE_VERSION_RET(Structure):
    pass

_S(struct_tagNET_DVR_ONLINEUPGRADE_VERSION_RET, [
    ('dwSize', DWORD),
    ('byNewVersionAvailable', BYTE),
    ('byNewVersion', BYTE * 64),
    ('byChangeLog', BYTE * 2048),
    ('byRes', BYTE * 971),
])

NET_DVR_ONLINEUPGRADE_VERSION_RET = struct_tagNET_DVR_ONLINEUPGRADE_VERSION_RET
LPNET_DVR_ONLINEUPGRADE_VERSION_RET = POINTER(struct_tagNET_DVR_ONLINEUPGRADE_VERSION_RET)
tagNET_DVR_ONLINEUPGRADE_VERSION_RET = struct_tagNET_DVR_ONLINEUPGRADE_VERSION_RET
