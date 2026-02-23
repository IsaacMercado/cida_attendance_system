from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ONLINEUPGRADE_VERSION_COND(Structure):
    pass

_S(struct_tagNET_DVR_ONLINEUPGRADE_VERSION_COND, [
    ('dwSize', DWORD),
    ('byCheckFromSvr', BYTE),
    ('byRes', BYTE * 59),
])

NET_DVR_ONLINEUPGRADE_VERSION_COND = struct_tagNET_DVR_ONLINEUPGRADE_VERSION_COND
LPNET_DVR_ONLINEUPGRADE_VERSION_COND = POINTER(struct_tagNET_DVR_ONLINEUPGRADE_VERSION_COND)
tagNET_DVR_ONLINEUPGRADE_VERSION_COND = struct_tagNET_DVR_ONLINEUPGRADE_VERSION_COND
