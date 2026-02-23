from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_pos_protocol_union import NET_DVR_POS_PROTOCOL_UNION


class struct_anon_419(Structure):
    pass

_S(struct_anon_419, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byCharSetType', BYTE),
    ('byRes1', BYTE),
    ('byProtocolType', BYTE),
    ('uPosProtocol', NET_DVR_POS_PROTOCOL_UNION),
    ('byRes', BYTE * 32),
])

NET_DVR_POS_FILTER_CFG = struct_anon_419
LPNET_DVR_POS_FILTER_CFG = POINTER(struct_anon_419)
