from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .anon_10 import NET_DVR_ETHERNET_V30


class struct_tagNET_DVR_ONE_BONDING(Structure):
    pass

_S(struct_tagNET_DVR_ONE_BONDING, [
    ('byMode', BYTE),
    ('byUseDhcp', BYTE),
    ('byMasterCard', BYTE),
    ('byStatus', BYTE),
    ('byBond', BYTE * 4),
    ('struEtherNet', NET_DVR_ETHERNET_V30),
    ('struGatewayIpAddr', NET_DVR_IPADDR),
    ('byEnableDNS', BYTE),
    ('byBondMode', BYTE),
    ('byRes1', BYTE * 2),
    ('byBond2', BYTE * 12),
    ('byRes', BYTE * 4),
])

NET_DVR_ONE_BONDING = struct_tagNET_DVR_ONE_BONDING
LPNET_DVR_ONE_BONDING = POINTER(struct_tagNET_DVR_ONE_BONDING)
tagNET_DVR_ONE_BONDING = struct_tagNET_DVR_ONE_BONDING
