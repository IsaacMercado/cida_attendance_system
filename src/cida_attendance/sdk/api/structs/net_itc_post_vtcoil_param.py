from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_geoglocation import NET_DVR_GEOGLOCATION
from .net_itc_plate_recog_param import NET_ITC_PLATE_RECOG_PARAM
from .net_itc_radar_param import NET_ITC_RADAR_PARAM
from .net_itc_vtcoil_info import NET_ITC_VTCOIL_INFO
from .net_vca_line import NET_VCA_LINE


class struct_tagNET_ITC_POST_VTCOIL_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_POST_VTCOIL_PARAM, [
    ('byRelatedLaneNum', BYTE),
    ('byIsDisplay', BYTE),
    ('byLoopPos', BYTE),
    ('byPolarLenType', BYTE),
    ('byDayAuxLightMode', BYTE),
    ('byVideoLaneNO', BYTE),
    ('byVideoLowTh', BYTE),
    ('byVideoHighTh', BYTE),
    ('byRecordMode', BYTE),
    ('bySnapMode', BYTE),
    ('bySpeedDetector', BYTE),
    ('byRes1', BYTE),
    ('wResolutionX', WORD),
    ('wResolutionY', WORD),
    ('dwDayInitExp', DWORD),
    ('dwDayMaxExp', DWORD),
    ('dwNightExp', DWORD),
    ('dwSnapExp', DWORD),
    ('byDayInitGain', BYTE),
    ('byDayMaxGain', BYTE),
    ('byNightGain', BYTE),
    ('bySnapGain', BYTE),
    ('dwSceneMode', DWORD),
    ('struGeogLocation', NET_DVR_GEOGLOCATION),
    ('struPlateRecog', NET_ITC_PLATE_RECOG_PARAM),
    ('struVtCoil', NET_ITC_VTCOIL_INFO * 5),
    ('struRadar', NET_ITC_RADAR_PARAM),
    ('struLine', NET_VCA_LINE),
    ('dwVioDetectType', DWORD),
    ('byDebugMode', BYTE),
    ('byRes', BYTE * 11),
])

NET_ITC_POST_VTCOIL_PARAM = struct_tagNET_ITC_POST_VTCOIL_PARAM
LPNET_ITC_POST_VTCOIL_PARAM = POINTER(struct_tagNET_ITC_POST_VTCOIL_PARAM)
tagNET_ITC_POST_VTCOIL_PARAM = struct_tagNET_ITC_POST_VTCOIL_PARAM
