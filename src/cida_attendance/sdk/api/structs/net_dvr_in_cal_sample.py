from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_dvr_line_segment import NET_DVR_LINE_SEGMENT
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_IN_CAL_SAMPLE(Structure):
    pass

_S(struct_tagNET_DVR_IN_CAL_SAMPLE, [
    ('struVcaRect', NET_VCA_RECT),
    ('struLineSegment', NET_DVR_LINE_SEGMENT),
])

NET_DVR_IN_CAL_SAMPLE = struct_tagNET_DVR_IN_CAL_SAMPLE
LPNET_DVR_IN_CAL_SAMPLE = POINTER(struct_tagNET_DVR_IN_CAL_SAMPLE)
tagNET_DVR_IN_CAL_SAMPLE = struct_tagNET_DVR_IN_CAL_SAMPLE
