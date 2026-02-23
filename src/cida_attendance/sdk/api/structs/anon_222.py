from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_219 import NET_DVR_ADAS_PICTURE_INFO
from .anon_220 import NET_DVR_ADAS_POSITION_INFO
from .anon_221 import NET_DVR_ADAS_ALARM_STATE
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_anon_222(Structure):
    pass

_S(struct_anon_222, [
    ('dwSize', DWORD),
    ('byChannel', BYTE),
    ('byRes1', BYTE * 3),
    ('struIpcInfo', NET_VCA_DEV_INFO),
    ('struPosInfo', NET_DVR_ADAS_POSITION_INFO),
    ('struPicInfo', NET_DVR_ADAS_PICTURE_INFO),
    ('struAlarmState', NET_DVR_ADAS_ALARM_STATE),
    ('byRes2', BYTE * 20),
])

NET_DVR_ADAS_ALRAM_INFO = struct_anon_222
LPNET_DVR_ADAS_ALRAM_INFO = POINTER(struct_anon_222)
