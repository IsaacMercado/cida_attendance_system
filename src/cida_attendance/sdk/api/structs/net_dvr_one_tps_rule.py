from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30
from .net_vca_polygon import NET_VCA_POLYGON
from .net_vca_size_filter import NET_VCA_SIZE_FILTER


class struct_tagNET_DVR_ONE_TPS_RULE(Structure):
    pass

_S(struct_tagNET_DVR_ONE_TPS_RULE, [
    ('byEnable', BYTE),
    ('byLaneID', BYTE),
    ('byRes1', BYTE * 2),
    ('dwCalcType', DWORD),
    ('struSizeFilter', NET_VCA_SIZE_FILTER),
    ('struVitrualLoop', NET_VCA_POLYGON),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 2) * 7),
    ('struHandleType', NET_DVR_HANDLEEXCEPTION_V30),
    ('byRes2', BYTE * 20),
])

NET_DVR_ONE_TPS_RULE = struct_tagNET_DVR_ONE_TPS_RULE
LPNET_DVR_ONE_TPS_RULE = POINTER(struct_tagNET_DVR_ONE_TPS_RULE)
tagNET_DVR_ONE_TPS_RULE = struct_tagNET_DVR_ONE_TPS_RULE
