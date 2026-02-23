from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_OPERATION_AUTH(Structure):
    pass

_S(struct_tagNET_DVR_OPERATION_AUTH, [
    ('dwSize', DWORD),
    ('byPassword', BYTE * 16),
    ('byRes', BYTE * 128),
])

NET_DVR_OPERATION_AUTH = struct_tagNET_DVR_OPERATION_AUTH
LPNET_DVR_OPERATION_AUTH = POINTER(struct_tagNET_DVR_OPERATION_AUTH)
tagNET_DVR_OPERATION_AUTH = struct_tagNET_DVR_OPERATION_AUTH
