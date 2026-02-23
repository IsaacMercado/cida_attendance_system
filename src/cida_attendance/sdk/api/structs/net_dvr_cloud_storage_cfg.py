from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CLOUD_STORAGE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CLOUD_STORAGE_CFG, [
    ('dwSize', DWORD),
    ('byEnableCS', BYTE),
    ('byRes', BYTE * 511),
])

NET_DVR_CLOUD_STORAGE_CFG = struct_tagNET_DVR_CLOUD_STORAGE_CFG
LPNET_DVR_CLOUD_STORAGE_CFG = POINTER(struct_tagNET_DVR_CLOUD_STORAGE_CFG)
tagNET_DVR_CLOUD_STORAGE_CFG = struct_tagNET_DVR_CLOUD_STORAGE_CFG
