from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_normal_schedtime import NET_DVR_NORMAL_SCHEDTIME


class struct_tagNET_DVR_SUBSYSTEM_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_SUBSYSTEM_ALARM, [
    ('dwSize', DWORD),
    ('struNormalSchedtime', (NET_DVR_NORMAL_SCHEDTIME * 8) * 7),
    ('byNormalSchedTimeOn', BYTE),
    ('byMandatoryAlarm', BYTE),
    ('byRes', BYTE * 254),
])

NET_DVR_SUBSYSTEM_ALARM = struct_tagNET_DVR_SUBSYSTEM_ALARM
LPNET_DVR_SUBSYSTEM_ALARM = POINTER(struct_tagNET_DVR_SUBSYSTEM_ALARM)
tagNET_DVR_SUBSYSTEM_ALARM = struct_tagNET_DVR_SUBSYSTEM_ALARM
