from ctypes import Union

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_holidate_modea import NET_DVR_HOLIDATE_MODEA
from .net_dvr_holidate_modeb import NET_DVR_HOLIDATE_MODEB
from .net_dvr_holidate_modec import NET_DVR_HOLIDATE_MODEC


class union_tagNET_DVR_HOLIDATE_UNION(Union):
    pass

_S(union_tagNET_DVR_HOLIDATE_UNION, [
    ('dwSize', DWORD * 3),
    ('struModeA', NET_DVR_HOLIDATE_MODEA),
    ('struModeB', NET_DVR_HOLIDATE_MODEB),
    ('struModeC', NET_DVR_HOLIDATE_MODEC),
])

NET_DVR_HOLIDATE_UNION = union_tagNET_DVR_HOLIDATE_UNION
LPNET_DVR_HOLIDATE_UNION = POINTER(union_tagNET_DVR_HOLIDATE_UNION)
tagNET_DVR_HOLIDATE_UNION = union_tagNET_DVR_HOLIDATE_UNION
