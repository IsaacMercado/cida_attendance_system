from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_card_port_state import NET_DVR_CARD_PORT_STATE


class struct_tagNET_DVR_NET_CARD_STATE(Structure):
    pass

_S(struct_tagNET_DVR_NET_CARD_STATE, [
    ('struNetPortState', NET_DVR_CARD_PORT_STATE * 4),
    ('byRes', BYTE * 64),
])

NET_DVR_NET_CARD_STATE = struct_tagNET_DVR_NET_CARD_STATE
LPNET_DVR_NET_CARD_STATE = POINTER(struct_tagNET_DVR_NET_CARD_STATE)
tagNET_DVR_NET_CARD_STATE = struct_tagNET_DVR_NET_CARD_STATE
