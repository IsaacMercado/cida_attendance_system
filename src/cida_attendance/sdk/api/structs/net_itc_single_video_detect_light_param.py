from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_pos_param import NET_POS_PARAM


class struct_tagNET_ITC_SINGLE_VIDEO_DETECT_LIGHT_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_SINGLE_VIDEO_DETECT_LIGHT_PARAM, [
    ('byLightNum', BYTE),
    ('byStraightLight', BYTE),
    ('byLeftLight', BYTE),
    ('byRightLight', BYTE),
    ('byRedLight', BYTE),
    ('byGreenLight', BYTE),
    ('byYellowLight', BYTE),
    ('byYellowLightTime', BYTE),
    ('struLightRect', NET_POS_PARAM),
    ('byRes', BYTE * 24),
])

NET_ITC_SINGLE_VIDEO_DETECT_LIGHT_PARAM = struct_tagNET_ITC_SINGLE_VIDEO_DETECT_LIGHT_PARAM
LPNET_ITC_SINGLE_VIDEO_DETECT_LIGHT_PARAM = POINTER(struct_tagNET_ITC_SINGLE_VIDEO_DETECT_LIGHT_PARAM)
tagNET_ITC_SINGLE_VIDEO_DETECT_LIGHT_PARAM = struct_tagNET_ITC_SINGLE_VIDEO_DETECT_LIGHT_PARAM
