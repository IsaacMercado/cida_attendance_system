from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RS485_CASCADE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_RS485_CASCADE_CFG, [
    ('dwSize', DWORD),
    ('byDevAddr', BYTE),
    ('byRes', BYTE * 131),
])

NET_DVR_RS485_CASCADE_CFG = struct_tagNET_DVR_RS485_CASCADE_CFG
LPNET_DVR_RS485_CASCADE_CFG = POINTER(struct_tagNET_DVR_RS485_CASCADE_CFG)
tagNET_DVR_RS485_CASCADE_CFG = struct_tagNET_DVR_RS485_CASCADE_CFG
