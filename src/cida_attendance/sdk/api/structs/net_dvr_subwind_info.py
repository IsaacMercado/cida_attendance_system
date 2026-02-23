from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_SUBWIND_INFO(Structure):
    pass

_S(struct__NET_DVR_SUBWIND_INFO, [
    ('dwSize', DWORD),
    ('dwSubWndNo', DWORD),
    ('byRes', BYTE * 8),
])

NET_DVR_SUBWIND_INFO = struct__NET_DVR_SUBWIND_INFO
LPNET_DVR_SUBWIND_INFO = POINTER(struct__NET_DVR_SUBWIND_INFO)
_NET_DVR_SUBWIND_INFO = struct__NET_DVR_SUBWIND_INFO
