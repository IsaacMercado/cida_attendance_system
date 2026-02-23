from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_user_info_v52 import NET_DVR_USER_INFO_V52


class struct_tagNET_DVR_USER_V52(Structure):
    pass

_S(struct_tagNET_DVR_USER_V52, [
    ('dwSize', DWORD),
    ('dwMaxUserNum', DWORD),
    ('struUser', NET_DVR_USER_INFO_V52 * 32),
    ('sloginPassword', c_char * 16),
    ('byRes', BYTE * 240),
])

NET_DVR_USER_V52 = struct_tagNET_DVR_USER_V52
LPNET_DVR_USER_V52 = POINTER(struct_tagNET_DVR_USER_V52)
tagNET_DVR_USER_V52 = struct_tagNET_DVR_USER_V52
