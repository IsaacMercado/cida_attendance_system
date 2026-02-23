from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PASSWORD_MANAGE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PASSWORD_MANAGE_CFG, [
    ('dwSize', DWORD),
    ('byRes', BYTE * 3),
    ('byLockCount', BYTE),
    ('dwLockTime', DWORD),
    ('byRes1', BYTE * 128),
])

NET_DVR_PASSWORD_MANAGE_CFG = struct_tagNET_DVR_PASSWORD_MANAGE_CFG
LPNET_DVR_PASSWORD_MANAGE_CFG = POINTER(struct_tagNET_DVR_PASSWORD_MANAGE_CFG)
tagNET_DVR_PASSWORD_MANAGE_CFG = struct_tagNET_DVR_PASSWORD_MANAGE_CFG
