from ctypes import Union

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_itc_video_epolice_param import NET_ITC_VIDEO_EPOLICE_PARAM


class union_tagNET_ITC_VIDEO_TRIGGER_PARAM_UNION(Union):
    pass

_S(union_tagNET_ITC_VIDEO_TRIGGER_PARAM_UNION, [
    ('uLen', DWORD * 1150),
    ('struVideoEP', NET_ITC_VIDEO_EPOLICE_PARAM),
])

NET_ITC_VIDEO_TRIGGER_PARAM_UNION = union_tagNET_ITC_VIDEO_TRIGGER_PARAM_UNION
LPNET_ITC_VIDEO_TRIGGER_PARAM_UNION = POINTER(union_tagNET_ITC_VIDEO_TRIGGER_PARAM_UNION)
tagNET_ITC_VIDEO_TRIGGER_PARAM_UNION = union_tagNET_ITC_VIDEO_TRIGGER_PARAM_UNION
