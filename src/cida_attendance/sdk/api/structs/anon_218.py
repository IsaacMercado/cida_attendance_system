from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_215 import NET_DVR_DBD_PICTURE_INFO
from .anon_216 import NET_DVR_DBD_POSITION_INFO
from .anon_217 import NET_DVR_DBD_ALARM_STATE
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_anon_218(Structure):
    pass

_S(struct_anon_218, [
    ('dwSize', DWORD),
    ('byChannel', BYTE),
    ('byLevel', BYTE),
    ('byRes1', BYTE * 2),
    ('struIpcInfo', NET_VCA_DEV_INFO),
    ('struPosInfo', NET_DVR_DBD_POSITION_INFO),
    ('struPicInfo', NET_DVR_DBD_PICTURE_INFO),
    ('struAlarmState', NET_DVR_DBD_ALARM_STATE),
    ('byRes2', BYTE * 20),
])

NET_DVR_DBD_ALRAM_INFO = struct_anon_218
LPNET_DVR_DBD_ALRAM_INFO = POINTER(struct_anon_218)
