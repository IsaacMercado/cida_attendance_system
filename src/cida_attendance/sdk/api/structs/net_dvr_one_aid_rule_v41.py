from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30
from .net_dvr_aid_param import NET_DVR_AID_PARAM
from .net_vca_polygon import NET_VCA_POLYGON
from .net_vca_size_filter import NET_VCA_SIZE_FILTER


class struct_tagNET_DVR_ONE_AID_RULE_V41(Structure):
    pass

_S(struct_tagNET_DVR_ONE_AID_RULE_V41, [
    ('byEnable', BYTE),
    ('byLaneNo', BYTE),
    ('byRes1', BYTE * 2),
    ('byRuleName', BYTE * 32),
    ('dwEventType', DWORD),
    ('struSizeFilter', NET_VCA_SIZE_FILTER),
    ('struPolygon', NET_VCA_POLYGON),
    ('struAIDParam', NET_DVR_AID_PARAM),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('struHandleType', NET_DVR_HANDLEEXCEPTION_V30),
    ('byRelRecordChan', BYTE * 128),
    ('byRes2', BYTE * 60),
])

NET_DVR_ONE_AID_RULE_V41 = struct_tagNET_DVR_ONE_AID_RULE_V41
LPNET_DVR_ONE_AID_RULE_V41 = POINTER(struct_tagNET_DVR_ONE_AID_RULE_V41)
tagNET_DVR_ONE_AID_RULE_V41 = struct_tagNET_DVR_ONE_AID_RULE_V41
