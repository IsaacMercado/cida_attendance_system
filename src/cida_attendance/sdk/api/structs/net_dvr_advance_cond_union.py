from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_object_feature import NET_DVR_OBJECT_FEATURE
from .net_vca_human_feature import NET_VCA_HUMAN_FEATURE


class union_tagNET_DVR_ADVANCE_COND_UNION(Union):
    pass

_S(union_tagNET_DVR_ADVANCE_COND_UNION, [
    ('byLen', BYTE * 36),
    ('struHumanFeature', NET_VCA_HUMAN_FEATURE),
    ('struObjectFeature', NET_DVR_OBJECT_FEATURE),
])

NET_DVR_ADVANCE_COND_UNION = union_tagNET_DVR_ADVANCE_COND_UNION
LPNET_DVR_ADVANCE_COND_UNION = POINTER(union_tagNET_DVR_ADVANCE_COND_UNION)
tagNET_DVR_ADVANCE_COND_UNION = union_tagNET_DVR_ADVANCE_COND_UNION
