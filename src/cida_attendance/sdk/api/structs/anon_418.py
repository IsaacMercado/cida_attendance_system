from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_411 import NET_DVR_POS_ACTION
from .net_dvr_pos_protocol_union import NET_DVR_POS_PROTOCOL_UNION


class struct_anon_418(Structure):
    pass

_S(struct_anon_418, [
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('sPosName', BYTE * 32),
    ('dwProtocolType', DWORD),
    ('struPosProtocol', NET_DVR_POS_PROTOCOL_UNION),
    ('struAction', NET_DVR_POS_ACTION),
    ('byRes', BYTE * 64),
])

NET_DVR_FILTER_CONFIG = struct_anon_418
LPNET_DVR_FILTER_CONFIG = POINTER(struct_anon_418)
