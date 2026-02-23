from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SHIPSCOUNT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SHIPSCOUNT_CFG, [
    ('dwSize', DWORD),
    ('dwUpShipsCount', DWORD),
    ('dwDownShipsCount', DWORD),
    ('dwLeftShipsCount', DWORD),
    ('dwRightShipsCount', DWORD),
    ('dwTotalCount', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('byDataType', BYTE),
    ('byRes', BYTE * 255),
])

NET_DVR_SHIPSCOUNT_CFG = struct_tagNET_DVR_SHIPSCOUNT_CFG
LPNET_DVR_SHIPSCOUNT_CFG = POINTER(struct_tagNET_DVR_SHIPSCOUNT_CFG)
tagNET_DVR_SHIPSCOUNT_CFG = struct_tagNET_DVR_SHIPSCOUNT_CFG
