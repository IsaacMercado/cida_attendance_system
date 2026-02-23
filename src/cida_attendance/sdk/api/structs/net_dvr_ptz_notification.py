from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_54 import NET_DVR_PRESETCHAN_INFO
from .anon_55 import NET_DVR_CRUISECHAN_INFO
from .anon_56 import NET_DVR_PTZTRACKCHAN_INFO


class struct_tagNET_DVR_PTZ_NOTIFICATION(Structure):
    pass

_S(struct_tagNET_DVR_PTZ_NOTIFICATION, [
    ('dwSize', DWORD),
    ('byEventType', WORD),
    ('byRes', BYTE * 62),
    ('dwEnablePresetChanNum', DWORD),
    ('struPresetChanInfo', NET_DVR_PRESETCHAN_INFO * 512),
    ('dwEnableCruiseChanNum', DWORD),
    ('struCruiseChanInfo', NET_DVR_CRUISECHAN_INFO * 512),
    ('dwEnablePtzTrackChanNum', DWORD),
    ('struPtzTrackInfo', NET_DVR_PTZTRACKCHAN_INFO * 512),
    ('byRes1', BYTE * 1024),
])

NET_DVR_PTZ_NOTIFICATION = struct_tagNET_DVR_PTZ_NOTIFICATION
LPNET_DVR_PTZ_NOTIFICATION = POINTER(struct_tagNET_DVR_PTZ_NOTIFICATION)
tagNET_DVR_PTZ_NOTIFICATION = struct_tagNET_DVR_PTZ_NOTIFICATION
