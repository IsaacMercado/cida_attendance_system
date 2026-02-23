from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_lldp_port_cfg import NET_DVR_LLDP_PORT_CFG


class struct_tagNET_DVR_LLDP_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LLDP_CFG, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('byRes1', BYTE * 3),
    ('dwHoldTime', DWORD),
    ('dwReiniTime', DWORD),
    ('dwPacketTime', DWORD),
    ('struLLDPPortCfg', NET_DVR_LLDP_PORT_CFG * 64),
    ('byRes2', BYTE * 32),
])

NET_DVR_LLDP_CFG = struct_tagNET_DVR_LLDP_CFG
LPNET_DVR_LLDP_CFG = POINTER(struct_tagNET_DVR_LLDP_CFG)
tagNET_DVR_LLDP_CFG = struct_tagNET_DVR_LLDP_CFG
