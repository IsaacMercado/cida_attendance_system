from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_REGISTER_RS485CFG(Structure):
    pass

_S(struct_tagNET_DVR_REGISTER_RS485CFG, [
    ('dwSize', DWORD),
    ('wDeviceProtocol', WORD),
    ('byRes', BYTE * 2),
    ('dwBaudRate', DWORD),
    ('byRes1', BYTE * 124),
])

NET_DVR_REGISTER_RS485CFG = struct_tagNET_DVR_REGISTER_RS485CFG
LPNET_DVR_REGISTER_RS485CFG = POINTER(struct_tagNET_DVR_REGISTER_RS485CFG)
tagNET_DVR_REGISTER_RS485CFG = struct_tagNET_DVR_REGISTER_RS485CFG
