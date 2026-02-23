from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_LOCAL_INPUT_INFO_(Structure):
    pass

_S(struct__NET_DVR_LOCAL_INPUT_INFO_, [
    ('dwSize', DWORD),
    ('byChannelName', BYTE * 32),
    ('byRes', BYTE * 32),
])

NET_DVR_LOCAL_INPUT_INFO = struct__NET_DVR_LOCAL_INPUT_INFO_
LPNET_DVR_LOCAL_INPUT_INFO = POINTER(struct__NET_DVR_LOCAL_INPUT_INFO_)
_NET_DVR_LOCAL_INPUT_INFO_ = struct__NET_DVR_LOCAL_INPUT_INFO_
