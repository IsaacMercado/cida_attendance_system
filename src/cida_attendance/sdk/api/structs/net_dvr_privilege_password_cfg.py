from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PRIVILEGE_PASSWORD_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PRIVILEGE_PASSWORD_CFG, [
    ('dwSize', DWORD),
    ('byPwdType', BYTE),
    ('byRes1', BYTE * 3),
    ('byOldPassword', BYTE * 16),
    ('byNewPassword', BYTE * 16),
    ('byRes2', BYTE * 128),
])

NET_DVR_PRIVILEGE_PASSWORD_CFG = struct_tagNET_DVR_PRIVILEGE_PASSWORD_CFG
LPNET_DVR_PRIVILEGE_PASSWORD_CFG = POINTER(struct_tagNET_DVR_PRIVILEGE_PASSWORD_CFG)
tagNET_DVR_PRIVILEGE_PASSWORD_CFG = struct_tagNET_DVR_PRIVILEGE_PASSWORD_CFG
