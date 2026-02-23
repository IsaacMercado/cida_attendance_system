from ctypes import Union

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_vca_advance_find import NET_VCA_ADVANCE_FIND
from .net_vca_normal_find import NET_VCA_NORMAL_FIND


class union_tagNET_VCA_FIND_SNAPPIC_UNION(Union):
    pass

_S(union_tagNET_VCA_FIND_SNAPPIC_UNION, [
    ('struNormalFind', NET_VCA_NORMAL_FIND),
    ('struAdvanceFind', NET_VCA_ADVANCE_FIND),
])

NET_VCA_FIND_SNAPPIC_UNION = union_tagNET_VCA_FIND_SNAPPIC_UNION
LPNET_VCA_FIND_SNAPPIC_UNION = POINTER(union_tagNET_VCA_FIND_SNAPPIC_UNION)
tagNET_VCA_FIND_SNAPPIC_UNION = union_tagNET_VCA_FIND_SNAPPIC_UNION
