from ctypes import Structure, c_float

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_HEATMAP_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_HEATMAP_PARAM, [
    ('byTargetTrackEnable', BYTE),
    ('bySensitivity', BYTE),
    ('byBackgroundUpdateRate', BYTE),
    ('bySceneChangeLevel', BYTE),
    ('byMinTargetSize', BYTE),
    ('byUploadHeatMapResultType', BYTE),
    ('byDayReport', BYTE),
    ('byWeekReport', BYTE),
    ('fConfidence', c_float),
    ('byMonthReport', BYTE),
    ('byYearReport', BYTE),
    ('byRes', BYTE * 6),
])

NET_DVR_HEATMAP_PARAM = struct_tagNET_DVR_HEATMAP_PARAM
LPNET_DVR_HEATMAP_PARAM = POINTER(struct_tagNET_DVR_HEATMAP_PARAM)
tagNET_DVR_HEATMAP_PARAM = struct_tagNET_DVR_HEATMAP_PARAM
