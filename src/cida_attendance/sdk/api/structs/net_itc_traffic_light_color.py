from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_TRAFFIC_LIGHT_COLOR(Structure):
    pass

_S(struct_tagNET_ITC_TRAFFIC_LIGHT_COLOR, [
    ('byLeftLight', BYTE),
    ('byRightLight', BYTE),
    ('byStraightLight', BYTE),
    ('byRes', BYTE * 45),
])

NET_ITC_TRAFFIC_LIGHT_COLOR = struct_tagNET_ITC_TRAFFIC_LIGHT_COLOR
LPNET_ITC_TRAFFIC_LIGHT_COLOR = POINTER(struct_tagNET_ITC_TRAFFIC_LIGHT_COLOR)
tagNET_ITC_TRAFFIC_LIGHT_COLOR = struct_tagNET_ITC_TRAFFIC_LIGHT_COLOR
