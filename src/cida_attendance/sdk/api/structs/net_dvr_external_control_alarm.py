from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .net_dvr_lamp_state import NET_DVR_LAMP_STATE


class struct_tagNET_DVR_EXTERNAL_CONTROL_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_EXTERNAL_CONTROL_ALARM, [
    ('dwSize', DWORD),
    ('dwChannelNo', DWORD),
    ('struLampStateCtrl', NET_DVR_LAMP_STATE),
    ('struExternalBeginTime', NET_DVR_TIME),
    ('byRes1', BYTE * 64),
])

NET_DVR_EXTERNAL_CONTROL_ALARM = struct_tagNET_DVR_EXTERNAL_CONTROL_ALARM
LPNET_DVR_EXTERNAL_CONTROL_ALARM = POINTER(struct_tagNET_DVR_EXTERNAL_CONTROL_ALARM)
tagNET_DVR_EXTERNAL_CONTROL_ALARM = struct_tagNET_DVR_EXTERNAL_CONTROL_ALARM
