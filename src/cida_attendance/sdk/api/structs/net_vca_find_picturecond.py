from ctypes import Structure

from ..base_classes import _S, BYTE, LONG
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_VCA_FIND_PICTURECOND(Structure):
    pass

_S(struct_tagNET_VCA_FIND_PICTURECOND, [
    ('lChannel', LONG),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
    ('byRes', BYTE * 12),
])

NET_VCA_FIND_PICTURECOND = struct_tagNET_VCA_FIND_PICTURECOND
LPNET_VCA_FIND_PICTURECOND = POINTER(struct_tagNET_VCA_FIND_PICTURECOND)
tagNET_VCA_FIND_PICTURECOND = struct_tagNET_VCA_FIND_PICTURECOND
