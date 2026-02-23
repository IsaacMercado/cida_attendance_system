from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_optical_dev_chan_info import NET_DVR_OPTICAL_DEV_CHAN_INFO


class struct_tagNET_DVR_OPTICAL_DEV_NODE(Structure):
    pass

_S(struct_tagNET_DVR_OPTICAL_DEV_NODE, [
    ('byValid', BYTE),
    ('byRes1', BYTE * 3),
    ('dwDevNo', DWORD),
    ('byDevName', BYTE * 32),
    ('byDevID', BYTE * 48),
    ('struChannel', NET_DVR_OPTICAL_DEV_CHAN_INFO * 16),
    ('byRes2', BYTE * 32),
])

NET_DVR_OPTICAL_DEV_NODE = struct_tagNET_DVR_OPTICAL_DEV_NODE
LPNET_DVR_OPTICAL_DEV_NODE = POINTER(struct_tagNET_DVR_OPTICAL_DEV_NODE)
tagNET_DVR_OPTICAL_DEV_NODE = struct_tagNET_DVR_OPTICAL_DEV_NODE
