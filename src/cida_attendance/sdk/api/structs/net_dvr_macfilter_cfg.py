from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MACFILTER_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MACFILTER_CFG, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('byPermissionType', BYTE),
    ('byRes1', BYTE * 2),
    ('szMacAddress', (BYTE * 6) * 48),
    ('byRes', BYTE * 128),
])

NET_DVR_MACFILTER_CFG = struct_tagNET_DVR_MACFILTER_CFG
LPNET_DVR_MACFILTER_CFG = POINTER(struct_tagNET_DVR_MACFILTER_CFG)
tagNET_DVR_MACFILTER_CFG = struct_tagNET_DVR_MACFILTER_CFG
