from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_direct_connect_chan_info import NET_DVR_DIRECT_CONNECT_CHAN_INFO


class struct_tagNET_DVR_AUTO_TRACK_CFG(Structure):
    pass

_S(struct_tagNET_DVR_AUTO_TRACK_CFG, [
    ('dwSize', DWORD),
    ('struSDIInfo', NET_DVR_DIRECT_CONNECT_CHAN_INFO * int((32 + 32))),
    ('byCameraType', BYTE * int((32 + 32))),
    ('byRes', BYTE * 64),
])

NET_DVR_AUTO_TRACK_CFG = struct_tagNET_DVR_AUTO_TRACK_CFG
LPNET_DVR_AUTO_TRACK_CFG = POINTER(struct_tagNET_DVR_AUTO_TRACK_CFG)
tagNET_DVR_AUTO_TRACK_CFG = struct_tagNET_DVR_AUTO_TRACK_CFG
