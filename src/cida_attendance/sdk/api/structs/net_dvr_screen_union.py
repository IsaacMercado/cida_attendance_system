from ctypes import Union

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_dvr_analogscreen import NET_DVR_ANALOGSCREEN
from .net_dvr_digitalscreen import NET_DVR_DIGITALSCREEN


class union_tagNET_DVR_SCREEN_UNION(Union):
    pass

_S(union_tagNET_DVR_SCREEN_UNION, [
    ('struDigitalScreen', NET_DVR_DIGITALSCREEN),
    ('struAnalogScreen', NET_DVR_ANALOGSCREEN),
])

NET_DVR_SCREEN_UNION = union_tagNET_DVR_SCREEN_UNION
LPNET_DVR_SCREEN_UNION = POINTER(union_tagNET_DVR_SCREEN_UNION)
tagNET_DVR_SCREEN_UNION = union_tagNET_DVR_SCREEN_UNION
