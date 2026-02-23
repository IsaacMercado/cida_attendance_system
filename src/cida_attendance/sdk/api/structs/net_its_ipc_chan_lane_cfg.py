from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_its_gate_lane_cfg import NET_ITS_GATE_LANE_CFG


class struct_tagNET_ITS_IPC_CHAN_LANE_CFG(Structure):
    pass

_S(struct_tagNET_ITS_IPC_CHAN_LANE_CFG, [
    ('dwSize', DWORD),
    ('byIpcType', BYTE),
    ('byRes', BYTE * 135),
    ('struGateLane', NET_ITS_GATE_LANE_CFG * 4),
])

NET_ITS_IPC_CHAN_LANE_CFG = struct_tagNET_ITS_IPC_CHAN_LANE_CFG
LPNET_ITS_IPC_CHAN_LANE_CFG = POINTER(struct_tagNET_ITS_IPC_CHAN_LANE_CFG)
tagNET_ITS_IPC_CHAN_LANE_CFG = struct_tagNET_ITS_IPC_CHAN_LANE_CFG
