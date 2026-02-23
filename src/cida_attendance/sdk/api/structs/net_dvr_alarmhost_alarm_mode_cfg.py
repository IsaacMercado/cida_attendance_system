from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_ALARM_MODE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_ALARM_MODE_CFG, [
    ('dwSize', DWORD),
    ('byDataUploadMode', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_ALARMHOST_ALARM_MODE_CFG = struct_tagNET_DVR_ALARMHOST_ALARM_MODE_CFG
LPNET_DVR_ALARMHOST_ALARM_MODE_CFG = POINTER(struct_tagNET_DVR_ALARMHOST_ALARM_MODE_CFG)
tagNET_DVR_ALARMHOST_ALARM_MODE_CFG = struct_tagNET_DVR_ALARMHOST_ALARM_MODE_CFG
