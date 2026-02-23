from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_fc_card_topology import NET_DVR_FC_CARD_TOPOLOGY


class struct_tagNET_DVR_FIBER_CONVERT_TOPOLOGY(Structure):
    pass

_S(struct_tagNET_DVR_FIBER_CONVERT_TOPOLOGY, [
    ('dwSize', DWORD),
    ('struFCCardTopology', NET_DVR_FC_CARD_TOPOLOGY * 33),
    ('byRes', BYTE * 64),
])

NET_DVR_FIBER_CONVERT_TOPOLOGY = struct_tagNET_DVR_FIBER_CONVERT_TOPOLOGY
LPNET_DVR_FIBER_CONVERT_TOPOLOGY = POINTER(struct_tagNET_DVR_FIBER_CONVERT_TOPOLOGY)
tagNET_DVR_FIBER_CONVERT_TOPOLOGY = struct_tagNET_DVR_FIBER_CONVERT_TOPOLOGY
