from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .net_dvr_pdc_enter_direction import NET_DVR_PDC_ENTER_DIRECTION
from .net_dvr_time_ex import NET_DVR_TIME_EX
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_PDC_RULE_CFG_V41(Structure):
    pass

_S(struct_tagNET_DVR_PDC_RULE_CFG_V41, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 23),
    ('struPolygon', NET_VCA_POLYGON),
    ('struEnterDirection', NET_DVR_PDC_ENTER_DIRECTION),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('struDayStartTime', NET_DVR_TIME_EX),
    ('struNightStartTime', NET_DVR_TIME_EX),
    ('byRes', BYTE * 100),
])

NET_DVR_PDC_RULE_CFG_V41 = struct_tagNET_DVR_PDC_RULE_CFG_V41
LPNET_DVR_PDC_RULE_CFG_V41 = POINTER(struct_tagNET_DVR_PDC_RULE_CFG_V41)
tagNET_DVR_PDC_RULE_CFG_V41 = struct_tagNET_DVR_PDC_RULE_CFG_V41
