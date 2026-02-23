from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_nat_port import NET_DVR_NAT_PORT


class struct_tagNET_DVR_NAT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_NAT_CFG, [
    ('dwSize', DWORD),
    ('wEnableUpnp', WORD),
    ('wEnableNat', WORD),
    ('struIpAddr', NET_DVR_IPADDR),
    ('struHttpPort', NET_DVR_NAT_PORT),
    ('struCmdPort', NET_DVR_NAT_PORT),
    ('struRtspPort', NET_DVR_NAT_PORT),
    ('byFriendName', BYTE * 64),
    ('byNatType', BYTE),
    ('byRes1', BYTE * 3),
    ('struHttpsPort', NET_DVR_NAT_PORT),
    ('struSDKOverTLSPort', NET_DVR_NAT_PORT),
    ('struRtspsPort', NET_DVR_NAT_PORT),
    ('byres', BYTE * 44),
])

NET_DVR_NAT_CFG = struct_tagNET_DVR_NAT_CFG
LPNET_DVR_NAT_CFG = POINTER(struct_tagNET_DVR_NAT_CFG)
tagNET_DVR_NAT_CFG = struct_tagNET_DVR_NAT_CFG
