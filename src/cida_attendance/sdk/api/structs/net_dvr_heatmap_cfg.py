from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .net_dvr_handleexception_v40 import NET_DVR_HANDLEEXCEPTION_V40
from .net_dvr_heatmap_param import NET_DVR_HEATMAP_PARAM
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_HEATMAP_CFG(Structure):
    pass

_S(struct_tagNET_DVR_HEATMAP_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes', BYTE * 3),
    ('struRegion', NET_VCA_POLYGON * 8),
    ('struHeatMap', NET_DVR_HEATMAP_PARAM),
    ('struHandleException', NET_DVR_HANDLEEXCEPTION_V40),
    ('struAlarmSched', (NET_DVR_SCHEDTIME * 8) * 7),
    ('byRes1', BYTE * 512),
])

NET_DVR_HEATMAP_CFG = struct_tagNET_DVR_HEATMAP_CFG
LPNET_DVR_HEATMAP_CFG = POINTER(struct_tagNET_DVR_HEATMAP_CFG)
tagNET_DVR_HEATMAP_CFG = struct_tagNET_DVR_HEATMAP_CFG
