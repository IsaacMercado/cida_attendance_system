from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_radar_info_param import NET_ITC_RADAR_INFO_PARAM


class union_tagNET_ITC_ACCESS_DEVINFO_PARAM_UNION(Union):
    pass

_S(union_tagNET_ITC_ACCESS_DEVINFO_PARAM_UNION, [
    ('uLen', BYTE * 128),
    ('struRadarInfoParam', NET_ITC_RADAR_INFO_PARAM),
])

NET_ITC_ACCESS_DEVINFO_PARAM_UNION = union_tagNET_ITC_ACCESS_DEVINFO_PARAM_UNION
LPNET_ITC_ACCESS_DEVINFO_PARAM_UNION = POINTER(union_tagNET_ITC_ACCESS_DEVINFO_PARAM_UNION)
tagNET_ITC_ACCESS_DEVINFO_PARAM_UNION = union_tagNET_ITC_ACCESS_DEVINFO_PARAM_UNION
