from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_GATE_CHARGEINFO(Structure):
    pass

_S(struct_tagNET_DVR_GATE_CHARGEINFO, [
    ('dwSize', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('sLicense', c_char * 16),
    ('szCardNo', c_char * 48),
    ('struEntranceTime', NET_DVR_TIME_V30),
    ('struDepartureTime', NET_DVR_TIME_V30),
    ('szDepartureID', c_char * 32),
    ('szEntranceID', c_char * 32),
    ('dwTotalCost', DWORD),
    ('szOperateName', c_char * 32),
    ('byChargeRuleId', BYTE),
    ('byVehicleType', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_GATE_CHARGEINFO = struct_tagNET_DVR_GATE_CHARGEINFO
LPNET_DVR_GATE_CHARGEINFO = POINTER(struct_tagNET_DVR_GATE_CHARGEINFO)
tagNET_DVR_GATE_CHARGEINFO = struct_tagNET_DVR_GATE_CHARGEINFO
