from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PXMULTICTRL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PXMULTICTRL_CFG, [
    ('dwSize', DWORD),
    ('dwMultiChansWaitTime', DWORD),
    ('byMultiChansCapEnabled', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_PXMULTICTRL_CFG = struct_tagNET_DVR_PXMULTICTRL_CFG
LPNET_DVR_PXMULTICTRL_CFG = POINTER(struct_tagNET_DVR_PXMULTICTRL_CFG)
tagNET_DVR_PXMULTICTRL_CFG = struct_tagNET_DVR_PXMULTICTRL_CFG
