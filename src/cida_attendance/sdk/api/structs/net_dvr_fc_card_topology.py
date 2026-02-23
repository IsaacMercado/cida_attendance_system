from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_fc_port_topology import NET_DVR_FC_PORT_TOPOLOGY


class struct_tagNET_DVR_FC_CARD_TOPOLOGY(Structure):
    pass

_S(struct_tagNET_DVR_FC_CARD_TOPOLOGY, [
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('dwCardNo', DWORD),
    ('dwSlotNum', DWORD),
    ('byTypeName', BYTE * 32),
    ('byLocalMac', BYTE * 6),
    ('struFCPortTopology', NET_DVR_FC_PORT_TOPOLOGY * 4),
    ('byRes', BYTE * 32),
])

NET_DVR_FC_CARD_TOPOLOGY = struct_tagNET_DVR_FC_CARD_TOPOLOGY
LPNET_DVR_FC_CARD_TOPOLOGY = POINTER(struct_tagNET_DVR_FC_CARD_TOPOLOGY)
tagNET_DVR_FC_CARD_TOPOLOGY = struct_tagNET_DVR_FC_CARD_TOPOLOGY
