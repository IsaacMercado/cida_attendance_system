from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ONE_KEY_CFG_SAN_V50(Structure):
    pass

_S(struct_tagNET_DVR_ONE_KEY_CFG_SAN_V50, [
    ('dwSize', DWORD),
    ('byRaidType', BYTE),
    ('bySpareRaidProportion', BYTE),
    ('byRes', BYTE * 254),
])

NET_DVR_ONE_KEY_CFG_SAN_V50 = struct_tagNET_DVR_ONE_KEY_CFG_SAN_V50
LPNET_DVR_ONE_KEY_CFG_SAN_V50 = POINTER(struct_tagNET_DVR_ONE_KEY_CFG_SAN_V50)
tagNET_DVR_ONE_KEY_CFG_SAN_V50 = struct_tagNET_DVR_ONE_KEY_CFG_SAN_V50
