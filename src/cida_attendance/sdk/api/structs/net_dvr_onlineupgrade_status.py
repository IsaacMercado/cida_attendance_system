from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ONLINEUPGRADE_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_ONLINEUPGRADE_STATUS, [
    ('dwSize', DWORD),
    ('byUpgradeStatus', BYTE),
    ('byProgress', BYTE),
    ('byRes', BYTE * 250),
])

NET_DVR_ONLINEUPGRADE_STATUS = struct_tagNET_DVR_ONLINEUPGRADE_STATUS
LPNET_DVR_ONLINEUPGRADE_STATUS = POINTER(struct_tagNET_DVR_ONLINEUPGRADE_STATUS)
tagNET_DVR_ONLINEUPGRADE_STATUS = struct_tagNET_DVR_ONLINEUPGRADE_STATUS
