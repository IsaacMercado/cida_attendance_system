from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CALL_WAITTING_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CALL_WAITTING_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE),
    ('wWaitTime', WORD),
    ('wCalledWaitTime', WORD),
    ('byRes', BYTE * 510),
])

NET_DVR_CALL_WAITTING_CFG = struct_tagNET_DVR_CALL_WAITTING_CFG
LPNET_DVR_CALL_WAITTING_CFG = POINTER(struct_tagNET_DVR_CALL_WAITTING_CFG)
tagNET_DVR_CALL_WAITTING_CFG = struct_tagNET_DVR_CALL_WAITTING_CFG
