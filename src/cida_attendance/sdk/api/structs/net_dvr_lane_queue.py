from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_LANE_QUEUE(Structure):
    pass

_S(struct_tagNET_DVR_LANE_QUEUE, [
    ('struHead', NET_VCA_POINT),
    ('struTail', NET_VCA_POINT),
    ('dwLength', DWORD),
])

NET_DVR_LANE_QUEUE = struct_tagNET_DVR_LANE_QUEUE
LPNET_DVR_LANE_QUEUE = POINTER(struct_tagNET_DVR_LANE_QUEUE)
tagNET_DVR_LANE_QUEUE = struct_tagNET_DVR_LANE_QUEUE
