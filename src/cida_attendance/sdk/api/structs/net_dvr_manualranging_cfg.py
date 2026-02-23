from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MANUALRANGING_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MANUALRANGING_CFG, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_MANUALRANGING_CFG = struct_tagNET_DVR_MANUALRANGING_CFG
LPNET_DVR_MANUALRANGING_CFG = POINTER(struct_tagNET_DVR_MANUALRANGING_CFG)
tagNET_DVR_MANUALRANGING_CFG = struct_tagNET_DVR_MANUALRANGING_CFG
