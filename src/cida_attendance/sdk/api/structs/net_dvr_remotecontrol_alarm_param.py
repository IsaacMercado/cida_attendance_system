from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_REMOTECONTROL_ALARM_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_REMOTECONTROL_ALARM_PARAM, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('wDealyTime', WORD),
    ('byRes', BYTE * 30),
])

NET_DVR_REMOTECONTROL_ALARM_PARAM = struct_tagNET_DVR_REMOTECONTROL_ALARM_PARAM
LPNET_DVR_REMOTECONTROL_ALARM_PARAM = POINTER(struct_tagNET_DVR_REMOTECONTROL_ALARM_PARAM)
tagNET_DVR_REMOTECONTROL_ALARM_PARAM = struct_tagNET_DVR_REMOTECONTROL_ALARM_PARAM
