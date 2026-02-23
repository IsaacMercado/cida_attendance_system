from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_BEHAVIOR_INFO(Structure):
    pass

_S(struct_tagNET_DVR_BEHAVIOR_INFO, [
    ('struVcaRect', NET_VCA_RECT),
    ('wPeopleNum', WORD),
    ('byRes2', BYTE * 238),
])

NET_DVR_BEHAVIOR_INFO = struct_tagNET_DVR_BEHAVIOR_INFO
LPNET_DVR_BEHAVIOR_INFO = POINTER(struct_tagNET_DVR_BEHAVIOR_INFO)
tagNET_DVR_BEHAVIOR_INFO = struct_tagNET_DVR_BEHAVIOR_INFO
