from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_wiper_continuework_param import NET_DVR_WIPER_CONTINUEWORK_PARAM


class union_tagNET_DVR_WIPERMODE_PARAM_UNION(Union):
    pass

_S(union_tagNET_DVR_WIPERMODE_PARAM_UNION, [
    ('uLen', BYTE * 16),
    ('struWiperContinueWorkParam', NET_DVR_WIPER_CONTINUEWORK_PARAM),
])

NET_DVR_WIPERMODE_PARAM_UNION = union_tagNET_DVR_WIPERMODE_PARAM_UNION
LPNET_DVR_WIPERMODE_PARAM_UNION = POINTER(union_tagNET_DVR_WIPERMODE_PARAM_UNION)
tagNET_DVR_WIPERMODE_PARAM_UNION = union_tagNET_DVR_WIPERMODE_PARAM_UNION
