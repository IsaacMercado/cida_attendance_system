from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_user_info_v40 import NET_DVR_USER_INFO_V40


class struct_tagNET_DVR_USER_V50(Structure):
    pass

_S(struct_tagNET_DVR_USER_V50, [
    ('dwSize', DWORD),
    ('dwMaxUserNum', DWORD),
    ('struUser', NET_DVR_USER_INFO_V40 * 32),
    ('sloginPassword', c_char * 16),
    ('byRes', BYTE * 240),
])

NET_DVR_USER_V50 = struct_tagNET_DVR_USER_V50
LPNET_DVR_USER_V50 = POINTER(struct_tagNET_DVR_USER_V50)
tagNET_DVR_USER_V50 = struct_tagNET_DVR_USER_V50
