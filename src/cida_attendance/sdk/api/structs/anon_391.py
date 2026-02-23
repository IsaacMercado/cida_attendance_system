from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .anon_389 import NET_DVR_MOTION_MULTI_AREA
from .anon_390 import NET_DVR_MOTION_SINGLE_AREA


class struct_anon_391(Structure):
    pass

_S(struct_anon_391, [
    ('struMotionSingleArea', NET_DVR_MOTION_SINGLE_AREA),
    ('struMotionMultiArea', NET_DVR_MOTION_MULTI_AREA),
])

NET_DVR_MOTION_MODE_PARAM = struct_anon_391
LPNET_DVR_MOTION_MODE_PARAM = POINTER(struct_anon_391)
