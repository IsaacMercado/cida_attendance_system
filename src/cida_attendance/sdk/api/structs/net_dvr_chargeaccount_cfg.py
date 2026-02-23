from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CHARGEACCOUNT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CHARGEACCOUNT_CFG, [
    ('dwSize', DWORD),
    ('fAccount', c_float),
    ('byRes', BYTE * 128),
])

NET_DVR_CHARGEACCOUNT_CFG = struct_tagNET_DVR_CHARGEACCOUNT_CFG
LPNET_DVR_CHARGEACCOUNT_CFG = POINTER(struct_tagNET_DVR_CHARGEACCOUNT_CFG)
tagNET_DVR_CHARGEACCOUNT_CFG = struct_tagNET_DVR_CHARGEACCOUNT_CFG
