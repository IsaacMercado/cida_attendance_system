from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_ALARM_PHONECFG(Structure):
    pass

_S(struct__NET_DVR_ALARM_PHONECFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('byPhoneNumber', BYTE * 32),
    ('dwArmRight', DWORD),
    ('dwDisArmRight', DWORD),
    ('dwClearAlarmRight', DWORD),
    ('byZoneReport', BYTE * 512),
    ('dwNonZoneReport', DWORD),
    ('byIntervalTime', BYTE),
    ('byRes2', BYTE),
    ('wDefineIntervalTime', WORD),
    ('byRes3', BYTE * 128),
])

NET_DVR_ALARM_PHONECFG = struct__NET_DVR_ALARM_PHONECFG
LPNET_DVR_ALARM_PHONECFG = POINTER(struct__NET_DVR_ALARM_PHONECFG)
_NET_DVR_ALARM_PHONECFG = struct__NET_DVR_ALARM_PHONECFG
