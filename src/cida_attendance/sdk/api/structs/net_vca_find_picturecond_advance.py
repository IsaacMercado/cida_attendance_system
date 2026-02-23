from ctypes import Structure

from ..base_classes import _S, BYTE, LONG
from ..ctypes_preamble import POINTER
from ..enums import VCA_FIND_SNAPPIC_TYPE
from .anon_1 import NET_DVR_TIME
from .net_vca_find_snappic_union import NET_VCA_FIND_SNAPPIC_UNION


class struct_tagNET_VCA_FIND_PICTURECOND_ADVANCE(Structure):
    pass

_S(struct_tagNET_VCA_FIND_PICTURECOND_ADVANCE, [
    ('lChannel', LONG),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
    ('byThreshold', BYTE),
    ('byRes', BYTE * 23),
    ('dwFindType', VCA_FIND_SNAPPIC_TYPE),
    ('uFindParam', NET_VCA_FIND_SNAPPIC_UNION),
])

NET_VCA_FIND_PICTURECOND_ADVANCE = struct_tagNET_VCA_FIND_PICTURECOND_ADVANCE
LPNET_VCA_FIND_PICTURECOND_ADVANCE = POINTER(struct_tagNET_VCA_FIND_PICTURECOND_ADVANCE)
tagNET_VCA_FIND_PICTURECOND_ADVANCE = struct_tagNET_VCA_FIND_PICTURECOND_ADVANCE
