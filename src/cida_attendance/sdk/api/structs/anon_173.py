from ctypes import Union, c_char

from ..base_classes import _S, BYTE
from .net_dvr_play_back_by_time import NET_DVR_PLAY_BACK_BY_TIME


class union_anon_173(Union):
    pass

_S(union_anon_173, [
    ('byRes', BYTE * 128),
    ('struPlayBackByTime', NET_DVR_PLAY_BACK_BY_TIME),
    ('sFileName', c_char * 128),
])

