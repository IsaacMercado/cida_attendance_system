from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BARRIERGATE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_BARRIERGATE_CFG, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byLaneNo', BYTE),
    ('byBarrierGateCtrl', BYTE),
    ('byEntranceNo', BYTE),
    ('byUnlock', BYTE),
    ('byRes', BYTE * 12),
])

NET_DVR_BARRIERGATE_CFG = struct_tagNET_DVR_BARRIERGATE_CFG
LPNET_DVR_BARRIERGATE_CFG = POINTER(struct_tagNET_DVR_BARRIERGATE_CFG)
tagNET_DVR_BARRIERGATE_CFG = struct_tagNET_DVR_BARRIERGATE_CFG
