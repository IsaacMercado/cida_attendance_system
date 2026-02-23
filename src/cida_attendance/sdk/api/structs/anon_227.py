from ctypes import Union

from ..base_classes import _S, DWORD
from .net_dvr_manual_ctrl_info import NET_DVR_MANUAL_CTRL_INFO


class union_anon_227(Union):
    pass

_S(union_anon_227, [
    ('dwULen', DWORD * 4),
    ('struManualCtrl', NET_DVR_MANUAL_CTRL_INFO),
])

