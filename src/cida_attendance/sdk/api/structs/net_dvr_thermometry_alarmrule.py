from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_thermometry_alarmrule_param import NET_DVR_THERMOMETRY_ALARMRULE_PARAM


class struct_tagNET_DVR_THERMOMETRY_ALARMRULE(Structure):
    pass

_S(struct_tagNET_DVR_THERMOMETRY_ALARMRULE, [
    ('dwSize', DWORD),
    ('struThermometryAlarmRuleParam', NET_DVR_THERMOMETRY_ALARMRULE_PARAM * 40),
    ('byRes', BYTE * 128),
])

NET_DVR_THERMOMETRY_ALARMRULE = struct_tagNET_DVR_THERMOMETRY_ALARMRULE
LPNET_DVR_THERMOMETRY_ALARMRULE = POINTER(struct_tagNET_DVR_THERMOMETRY_ALARMRULE)
tagNET_DVR_THERMOMETRY_ALARMRULE = struct_tagNET_DVR_THERMOMETRY_ALARMRULE
