from ctypes import Union

from ..base_classes import _S, BYTE
from .net_dvr_play_back_by_time import NET_DVR_PLAY_BACK_BY_TIME


class union_anon_175(Union):
    pass

_S(union_anon_175, [
    ('byRes', BYTE * 128),
    ('struPlayBackByTime', NET_DVR_PLAY_BACK_BY_TIME),
    ('sFileName', BYTE * 128),
])

