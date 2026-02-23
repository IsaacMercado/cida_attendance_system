from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_OPTICAL_DEV_CHAN_INFO(Structure):
    pass

_S(struct_tagNET_DVR_OPTICAL_DEV_CHAN_INFO, [
    ('dwChannel', DWORD),
    ('byChannelName', BYTE * 32),
    ('bySignal', BYTE),
    ('bySignalType', BYTE),
    ('byRes', BYTE * 10),
])

NET_DVR_OPTICAL_DEV_CHAN_INFO = struct_tagNET_DVR_OPTICAL_DEV_CHAN_INFO
LPNET_DVR_OPTICAL_DEV_CHAN_INFO = POINTER(struct_tagNET_DVR_OPTICAL_DEV_CHAN_INFO)
tagNET_DVR_OPTICAL_DEV_CHAN_INFO = struct_tagNET_DVR_OPTICAL_DEV_CHAN_INFO
