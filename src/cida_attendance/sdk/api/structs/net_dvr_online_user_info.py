from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ONLINE_USER_INFO_(Structure):
    pass

_S(struct_tagNET_DVR_ONLINE_USER_INFO_, [
    ('dwSize', DWORD),
    ('wOnlineUserCount', WORD),
    ('byRes', BYTE * 514),
])

NET_DVR_ONLINE_USER_INFO = struct_tagNET_DVR_ONLINE_USER_INFO_
LPNET_DVR_ONLINE_USER_INFO = POINTER(struct_tagNET_DVR_ONLINE_USER_INFO_)
tagNET_DVR_ONLINE_USER_INFO_ = struct_tagNET_DVR_ONLINE_USER_INFO_
