from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_lane_param_v41 import NET_DVR_LANE_PARAM_V41


class struct_tagNET_DVR_TPS_INFO_V41(Structure):
    pass

_S(struct_tagNET_DVR_TPS_INFO_V41, [
    ('dwLanNum', DWORD),
    ('struLaneParam', NET_DVR_LANE_PARAM_V41 * 8),
    ('dwSceneID', DWORD),
    ('byRes', BYTE * 28),
])

NET_DVR_TPS_INFO_V41 = struct_tagNET_DVR_TPS_INFO_V41
LPNET_DVR_TPS_INFO_V41 = POINTER(struct_tagNET_DVR_TPS_INFO_V41)
tagNET_DVR_TPS_INFO_V41 = struct_tagNET_DVR_TPS_INFO_V41
