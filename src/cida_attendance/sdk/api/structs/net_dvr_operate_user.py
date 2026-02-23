from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_OPERATE_USER(Structure):
    pass

_S(struct_tagNET_DVR_OPERATE_USER, [
    ('dwSize', DWORD),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('bySubSystemPermission', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_OPERATE_USER = struct_tagNET_DVR_OPERATE_USER
LPNET_DVR_OPERATE_USER = POINTER(struct_tagNET_DVR_OPERATE_USER)
tagNET_DVR_OPERATE_USER = struct_tagNET_DVR_OPERATE_USER
