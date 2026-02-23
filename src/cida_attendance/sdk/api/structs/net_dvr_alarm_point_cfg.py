from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_alarm_point_param_union import NET_DVR_ALARM_POINT_PARAM_UNION


class struct_tagNET_DVR_ALARM_POINT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARM_POINT_CFG, [
    ('dwSize', DWORD),
    ('dwPointNo', DWORD),
    ('sPointDescribe', BYTE * 32),
    ('struPointParam', NET_DVR_ALARM_POINT_PARAM_UNION),
    ('byPointType', BYTE),
    ('byChanType', BYTE),
    ('byRes1', BYTE * 2),
    ('dwChanNo', DWORD),
    ('dwSubChanNo', DWORD),
    ('dwVariableNo', DWORD),
    ('byRes', BYTE * 16),
])

NET_DVR_ALARM_POINT_CFG = struct_tagNET_DVR_ALARM_POINT_CFG
LPNET_DVR_ALARM_POINT_CFG = POINTER(struct_tagNET_DVR_ALARM_POINT_CFG)
tagNET_DVR_ALARM_POINT_CFG = struct_tagNET_DVR_ALARM_POINT_CFG
