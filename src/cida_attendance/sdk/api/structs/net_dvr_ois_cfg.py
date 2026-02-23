from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_OIS_CFG(Structure):
    pass

_S(struct_tagNET_DVR_OIS_CFG, [
    ('dwSize', DWORD),
    ('byMode', BYTE),
    ('byOISLevel', BYTE),
    ('byOISSensitivity', BYTE),
    ('byRes', BYTE * 125),
])

NET_DVR_OIS_CFG = struct_tagNET_DVR_OIS_CFG
LPNET_DVR_OIS_CFG = POINTER(struct_tagNET_DVR_OIS_CFG)
tagNET_DVR_OIS_CFG = struct_tagNET_DVR_OIS_CFG
