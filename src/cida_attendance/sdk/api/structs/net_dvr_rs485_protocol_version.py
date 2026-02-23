from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RS485_PROTOCOL_VERSION(Structure):
    pass

_S(struct_tagNET_DVR_RS485_PROTOCOL_VERSION, [
    ('dwSize', DWORD),
    ('byProtocleVersion', BYTE * 32),
    ('byRes', BYTE * 128),
])

NET_DVR_RS485_PROTOCOL_VERSION = struct_tagNET_DVR_RS485_PROTOCOL_VERSION
LPNET_DVR_RS485_PROTOCOL_VESRION = POINTER(struct_tagNET_DVR_RS485_PROTOCOL_VERSION)
tagNET_DVR_RS485_PROTOCOL_VERSION = struct_tagNET_DVR_RS485_PROTOCOL_VERSION
