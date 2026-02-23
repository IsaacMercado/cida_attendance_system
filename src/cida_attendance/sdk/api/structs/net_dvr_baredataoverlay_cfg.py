from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BAREDATAOVERLAY_CFG(Structure):
    pass

_S(struct_tagNET_DVR_BAREDATAOVERLAY_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byIntervalTime', BYTE),
    ('byRes', BYTE * 258),
])

NET_DVR_BAREDATAOVERLAY_CFG = struct_tagNET_DVR_BAREDATAOVERLAY_CFG
LPNET_DVR_BAREDATAOVERLAY_CFG = POINTER(struct_tagNET_DVR_BAREDATAOVERLAY_CFG)
tagNET_DVR_BAREDATAOVERLAY_CFG = struct_tagNET_DVR_BAREDATAOVERLAY_CFG
