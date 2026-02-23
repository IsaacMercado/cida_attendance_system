from ctypes import Structure, c_float

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_EVENT_PARAM_UNION(Structure):
    pass

_S(struct_tagNET_DVR_EVENT_PARAM_UNION, [
    ('uLen', DWORD * 3),
    ('dwHumanIn', DWORD),
    ('fCrowdDensity', c_float),
])

NET_DVR_EVENT_PARAM_UNION = struct_tagNET_DVR_EVENT_PARAM_UNION
LPNET_DVR_EVENT_PARAM_UNION = POINTER(struct_tagNET_DVR_EVENT_PARAM_UNION)
tagNET_DVR_EVENT_PARAM_UNION = struct_tagNET_DVR_EVENT_PARAM_UNION
