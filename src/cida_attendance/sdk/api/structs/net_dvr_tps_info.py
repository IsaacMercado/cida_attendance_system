from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_lane_param import NET_DVR_LANE_PARAM


class struct_tagNET_DVR_TPS_INFO(Structure):
    pass

_S(struct_tagNET_DVR_TPS_INFO, [
    ('dwLanNum', DWORD),
    ('struLaneParam', NET_DVR_LANE_PARAM * 8),
])

NET_DVR_TPS_INFO = struct_tagNET_DVR_TPS_INFO
LPNET_DVR_TPS_INFO = POINTER(struct_tagNET_DVR_TPS_INFO)
tagNET_DVR_TPS_INFO = struct_tagNET_DVR_TPS_INFO
