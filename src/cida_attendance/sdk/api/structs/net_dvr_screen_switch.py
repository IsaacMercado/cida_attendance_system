from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_SCREEN_SWITCH_(Structure):
    pass

_S(struct__NET_DVR_SCREEN_SWITCH_, [
    ('dwSize', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_SCREEN_SWITCH = struct__NET_DVR_SCREEN_SWITCH_
LPNET_DVR_SCREEN_SWITCH = POINTER(struct__NET_DVR_SCREEN_SWITCH_)
_NET_DVR_SCREEN_SWITCH_ = struct__NET_DVR_SCREEN_SWITCH_
