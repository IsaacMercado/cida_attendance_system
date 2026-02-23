from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_geoglocation import NET_DVR_GEOGLOCATION
from .net_dvr_trigcoordinate import NET_DVR_TRIGCOORDINATE


class struct_tagNET_DVR_VTPARAM(Structure):
    pass

_S(struct_tagNET_DVR_VTPARAM, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byIsDisplay', BYTE),
    ('byLoopPos', BYTE),
    ('bySnapGain', BYTE),
    ('dwSnapShutter', DWORD),
    ('struTrigCoordinate', NET_DVR_TRIGCOORDINATE),
    ('struRes', NET_DVR_TRIGCOORDINATE * 5),
    ('byTotalLaneNum', BYTE),
    ('byPolarLenType', BYTE),
    ('byDayAuxLightMode', BYTE),
    ('byLoopToCalRoadBright', BYTE),
    ('byRoadGrayLowTh', BYTE),
    ('byRoadGrayHighTh', BYTE),
    ('wLoopPosBias', WORD),
    ('dwHfrShtterInitValue', DWORD),
    ('dwSnapShtterInitValue', DWORD),
    ('dwHfrShtterMaxValue', DWORD),
    ('dwSnapShtterMaxValue', DWORD),
    ('dwHfrShtterNightValue', DWORD),
    ('dwSnapShtterNightMinValue', DWORD),
    ('dwSnapShtterNightMaxValue', DWORD),
    ('dwInitAfe', DWORD),
    ('dwMaxAfe', DWORD),
    ('wResolutionX', WORD),
    ('wResolutionY', WORD),
    ('dwGainNightValue', DWORD),
    ('dwSceneMode', DWORD),
    ('dwRecordMode', DWORD),
    ('struGeogLocation', NET_DVR_GEOGLOCATION),
    ('byTrigFlag', BYTE * 5),
    ('byTrigSensitive', BYTE * 5),
    ('byRes2', BYTE * 62),
])

NET_DVR_VTPARAM = struct_tagNET_DVR_VTPARAM
LPNET_DVR_VTPARAM = POINTER(struct_tagNET_DVR_VTPARAM)
tagNET_DVR_VTPARAM = struct_tagNET_DVR_VTPARAM
