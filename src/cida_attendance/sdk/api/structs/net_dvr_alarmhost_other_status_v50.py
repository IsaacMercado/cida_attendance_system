from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_OTHER_STATUS_V50(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_OTHER_STATUS_V50, [
    ('dwSize', DWORD),
    ('bySirenStatus', BYTE * 8),
    ('byDetetorPower', BYTE * 128),
    ('byDetetorConnection', BYTE * 128),
    ('bySirenPower', BYTE * 8),
    ('bySirenTamperStatus', BYTE * 8),
    ('byPowerStausEnabled', BYTE * int((128 / 8))),
    ('byDetetorPowerStatus', BYTE * int((128 / 8))),
    ('byDetetorPowerType', BYTE),
    ('byRes', BYTE * 975),
])

NET_DVR_ALARMHOST_OTHER_STATUS_V50 = struct_tagNET_DVR_ALARMHOST_OTHER_STATUS_V50
LPNET_DVR_ALARMHOST_OTHER_STATUS_V50 = POINTER(struct_tagNET_DVR_ALARMHOST_OTHER_STATUS_V50)
tagNET_DVR_ALARMHOST_OTHER_STATUS_V50 = struct_tagNET_DVR_ALARMHOST_OTHER_STATUS_V50
