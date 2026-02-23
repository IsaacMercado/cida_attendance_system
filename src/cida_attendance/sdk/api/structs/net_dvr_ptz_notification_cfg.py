from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_54 import NET_DVR_PRESETCHAN_INFO
from .anon_55 import NET_DVR_CRUISECHAN_INFO
from .anon_56 import NET_DVR_PTZTRACKCHAN_INFO


class struct_tagNET_DVR_PTZ_NOTIFICATION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PTZ_NOTIFICATION_CFG, [
    ('dwSize', DWORD),
    ('dwEnablePresetChanNum', DWORD),
    ('struPresetChanInfo', NET_DVR_PRESETCHAN_INFO * 512),
    ('dwEnableCruiseChanNum', DWORD),
    ('struCruiseChanInfo', NET_DVR_CRUISECHAN_INFO * 512),
    ('dwEnablePtzTrackChanNum', DWORD),
    ('struPtzTrackInfo', NET_DVR_PTZTRACKCHAN_INFO * 512),
    ('byRes1', BYTE * 1024),
])

NET_DVR_PTZ_NOTIFICATION_CFG = struct_tagNET_DVR_PTZ_NOTIFICATION_CFG
LPNET_DVR_PTZ_NOTIFICATION_CFG = POINTER(struct_tagNET_DVR_PTZ_NOTIFICATION_CFG)
tagNET_DVR_PTZ_NOTIFICATION_CFG = struct_tagNET_DVR_PTZ_NOTIFICATION_CFG
