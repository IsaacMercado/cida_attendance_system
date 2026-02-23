from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_user_info_v40 import NET_DVR_USER_INFO_V40


class struct_tagNET_DVR_USER_V40(Structure):
    pass

_S(struct_tagNET_DVR_USER_V40, [
    ('dwSize', DWORD),
    ('dwMaxUserNum', DWORD),
    ('struUser', NET_DVR_USER_INFO_V40 * 32),
])

NET_DVR_USER_V40 = struct_tagNET_DVR_USER_V40
LPNET_DVR_USER_V40 = POINTER(struct_tagNET_DVR_USER_V40)
tagNET_DVR_USER_V40 = struct_tagNET_DVR_USER_V40
