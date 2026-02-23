from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_atmfindinfo import NET_DVR_ATMFINDINFO


class union_tagNET_DVR_SPECIAL_FINDINFO_UNION(Union):
    pass

_S(union_tagNET_DVR_SPECIAL_FINDINFO_UNION, [
    ('byLenth', BYTE * 8),
    ('struATMFindInfo', NET_DVR_ATMFINDINFO),
])

NET_DVR_SPECIAL_FINDINFO_UNION = union_tagNET_DVR_SPECIAL_FINDINFO_UNION
LPNET_DVR_SPECIAL_FINDINFO_UNION = POINTER(union_tagNET_DVR_SPECIAL_FINDINFO_UNION)
tagNET_DVR_SPECIAL_FINDINFO_UNION = union_tagNET_DVR_SPECIAL_FINDINFO_UNION
