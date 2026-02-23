from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_TRAFFIC_LIGHT_TURN(Structure):
    pass

_S(struct_tagNET_ITC_TRAFFIC_LIGHT_TURN, [
    ('byLightType', BYTE * 6),
    ('byRes', BYTE * 42),
])

NET_ITC_TRAFFIC_LIGHT_TURN = struct_tagNET_ITC_TRAFFIC_LIGHT_TURN
LPNET_ITC_TRAFFIC_LIGHT_TURN = POINTER(struct_tagNET_ITC_TRAFFIC_LIGHT_TURN)
tagNET_ITC_TRAFFIC_LIGHT_TURN = struct_tagNET_ITC_TRAFFIC_LIGHT_TURN
