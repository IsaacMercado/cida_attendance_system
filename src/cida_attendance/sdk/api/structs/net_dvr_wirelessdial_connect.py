from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WIRELESSDIAL_CONNECT(Structure):
    pass

_S(struct_tagNET_DVR_WIRELESSDIAL_CONNECT, [
    ('dwSize', DWORD),
    ('dwInterface', DWORD),
    ('byEnableConnect', BYTE),
    ('byRes', BYTE * 255),
])

NET_DVR_WIRELESSDIAL_CONNECT_PARAM = struct_tagNET_DVR_WIRELESSDIAL_CONNECT
LPNET_DVR_WIRELESSDIAL_CONNECT_PARAM = POINTER(struct_tagNET_DVR_WIRELESSDIAL_CONNECT)
tagNET_DVR_WIRELESSDIAL_CONNECT = struct_tagNET_DVR_WIRELESSDIAL_CONNECT
