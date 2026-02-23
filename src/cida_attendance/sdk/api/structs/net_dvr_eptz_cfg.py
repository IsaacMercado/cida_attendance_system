from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_EPTZ_CFG(Structure):
    pass

_S(struct_tagNET_DVR_EPTZ_CFG, [
    ('dwSize', DWORD),
    ('byEnableEPTZ', BYTE),
    ('byRes', BYTE * 503),
])

NET_DVR_EPTZ_CFG = struct_tagNET_DVR_EPTZ_CFG
LPNET_DVR_EPTZ_CFG = POINTER(struct_tagNET_DVR_EPTZ_CFG)
tagNET_DVR_EPTZ_CFG = struct_tagNET_DVR_EPTZ_CFG
