from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ONLINEUPGRADE_SERVER(Structure):
    pass

_S(struct_tagNET_DVR_ONLINEUPGRADE_SERVER, [
    ('dwSize', DWORD),
    ('byConnectStatus', BYTE),
    ('byRes', BYTE * 1019),
])

NET_DVR_ONLINEUPGRADE_SERVER = struct_tagNET_DVR_ONLINEUPGRADE_SERVER
LPNET_DVR_ONLINEUPGRADE_SERVER = POINTER(struct_tagNET_DVR_ONLINEUPGRADE_SERVER)
tagNET_DVR_ONLINEUPGRADE_SERVER = struct_tagNET_DVR_ONLINEUPGRADE_SERVER
