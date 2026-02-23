from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_GATEWAY_CFG(Structure):
    pass

_S(struct_tagNET_DVR_GATEWAY_CFG, [
    ('dwSize', DWORD),
    ('byName', BYTE * 32),
    ('byEnable', BYTE),
    ('byLocalEnable', BYTE),
    ('wDelayTime', WORD),
    ('byLockWorkMode', BYTE),
    ('byRes2', BYTE * 31),
])

NET_DVR_GATEWAY_CFG = struct_tagNET_DVR_GATEWAY_CFG
LPNET_DVR_GATEWAY_CFG = POINTER(struct_tagNET_DVR_GATEWAY_CFG)
tagNET_DVR_GATEWAY_CFG = struct_tagNET_DVR_GATEWAY_CFG
