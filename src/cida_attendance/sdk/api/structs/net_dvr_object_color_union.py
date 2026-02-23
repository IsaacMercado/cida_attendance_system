from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_26 import NET_DVR_COLOR
from .net_dvr_pic import NET_DVR_PIC


class union_tagNET_DVR_OBJECT_COLOR_UNION(Union):
    pass

_S(union_tagNET_DVR_OBJECT_COLOR_UNION, [
    ('struColor', NET_DVR_COLOR),
    ('struPicture', NET_DVR_PIC),
    ('byRes', BYTE * 64),
])

NET_DVR_OBJECT_COLOR_UNION = union_tagNET_DVR_OBJECT_COLOR_UNION
LPNET_DVR_OBJECT_COLOR_UNION = POINTER(union_tagNET_DVR_OBJECT_COLOR_UNION)
tagNET_DVR_OBJECT_COLOR_UNION = union_tagNET_DVR_OBJECT_COLOR_UNION
