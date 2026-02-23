from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DVCS_STATE_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_DVCS_STATE_ALARM, [
    ('dwSize', DWORD),
    ('byAlarmType', BYTE),
    ('byDeviceType', BYTE),
    ('byWallNo', BYTE),
    ('byDeviceChanIndex', BYTE),
    ('dwDeviceIndex', DWORD),
    ('wResolutionX', WORD),
    ('wResolutionY', WORD),
    ('wTemperature', WORD),
    ('byRes', BYTE * 86),
])

NET_DVR_DVCS_STATE_ALARM = struct_tagNET_DVR_DVCS_STATE_ALARM
LPNET_DVR_DVCS_STATE_ALARM = POINTER(struct_tagNET_DVR_DVCS_STATE_ALARM)
tagNET_DVR_DVCS_STATE_ALARM = struct_tagNET_DVR_DVCS_STATE_ALARM
