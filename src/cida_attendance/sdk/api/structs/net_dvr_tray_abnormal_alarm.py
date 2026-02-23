from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_TRAY_ABNORMAL_ALARM_(Structure):
    pass

_S(struct__NET_DVR_TRAY_ABNORMAL_ALARM_, [
    ('dwSize', DWORD),
    ('dwAlarmType', DWORD),
    ('byTrayNo', BYTE),
    ('byRes', BYTE * 3),
    ('dwInquestTime', DWORD),
    ('dwNotifyChannel', DWORD),
    ('byRes1', BYTE * 244),
])

NET_DVR_INQUEST_ALARM = struct__NET_DVR_TRAY_ABNORMAL_ALARM_
LPNET_DVR_TRAY_ABNORMAL_ALARM = POINTER(struct__NET_DVR_TRAY_ABNORMAL_ALARM_)
_NET_DVR_TRAY_ABNORMAL_ALARM_ = struct__NET_DVR_TRAY_ABNORMAL_ALARM_
