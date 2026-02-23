from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DATA_CALLBACK_CFG(Structure):
    pass

_S(struct_tagNET_DVR_DATA_CALLBACK_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byDelData', BYTE),
    ('byRes', BYTE * 30),
])

NET_DVR_DATA_CALLBACK_CFG = struct_tagNET_DVR_DATA_CALLBACK_CFG
LPNET_DVR_DATA_CALLBACK_CFG = POINTER(struct_tagNET_DVR_DATA_CALLBACK_CFG)
tagNET_DVR_DATA_CALLBACK_CFG = struct_tagNET_DVR_DATA_CALLBACK_CFG
