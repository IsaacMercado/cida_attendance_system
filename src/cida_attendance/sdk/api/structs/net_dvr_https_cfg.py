from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_HTTPS_CFG(Structure):
    pass

_S(struct_tagNET_DVR_HTTPS_CFG, [
    ('dwSize', DWORD),
    ('wHttpsPort', WORD),
    ('byEnable', BYTE),
    ('byRes', BYTE * 125),
])

NET_DVR_HTTPS_CFG = struct_tagNET_DVR_HTTPS_CFG
LPNET_DVR_HTTPS_CFG = POINTER(struct_tagNET_DVR_HTTPS_CFG)
tagNET_DVR_HTTPS_CFG = struct_tagNET_DVR_HTTPS_CFG
