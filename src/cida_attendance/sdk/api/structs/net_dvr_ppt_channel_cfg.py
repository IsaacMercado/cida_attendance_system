from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_PPT_CHANNEL_CFG_(Structure):
    pass

_S(struct__NET_DVR_PPT_CHANNEL_CFG_, [
    ('dwSize', DWORD),
    ('byChan', BYTE * 128),
    ('byRes', BYTE * 32),
])

NET_DVR_PPT_CHANNEL_CFG = struct__NET_DVR_PPT_CHANNEL_CFG_
LPNET_DVR_PPT_CHANNEL_CFG = POINTER(struct__NET_DVR_PPT_CHANNEL_CFG_)
_NET_DVR_PPT_CHANNEL_CFG_ = struct__NET_DVR_PPT_CHANNEL_CFG_
