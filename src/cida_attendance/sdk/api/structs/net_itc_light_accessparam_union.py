from ctypes import Union

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_itc_io_light_param import NET_ITC_IO_LIGHT_PARAM
from .net_itc_rs485_light_param import NET_ITC_RS485_LIGHT_PARAM
from .net_itc_video_detect_light_param import NET_ITC_VIDEO_DETECT_LIGHT_PARAM


class union_tagNET_ITC_LIGHT_ACCESSPARAM_UNION(Union):
    pass

_S(union_tagNET_ITC_LIGHT_ACCESSPARAM_UNION, [
    ('uLen', DWORD * 122),
    ('struIOLight', NET_ITC_IO_LIGHT_PARAM),
    ('struRS485Light', NET_ITC_RS485_LIGHT_PARAM),
    ('struVideoDelectLight', NET_ITC_VIDEO_DETECT_LIGHT_PARAM),
])

NET_ITC_LIGHT_ACCESSPARAM_UNION = union_tagNET_ITC_LIGHT_ACCESSPARAM_UNION
LPNET_ITC_LIGHT_ACCESSPARAM_UNION = POINTER(union_tagNET_ITC_LIGHT_ACCESSPARAM_UNION)
tagNET_ITC_LIGHT_ACCESSPARAM_UNION = union_tagNET_ITC_LIGHT_ACCESSPARAM_UNION
