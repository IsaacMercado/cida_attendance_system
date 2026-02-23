from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .anon_12 import NET_DVR_PPPOECFG
from .anon_14 import NET_DVR_ETHERNET_MULTI


class struct_anon_15(Structure):
    pass

_S(struct_anon_15, [
    ('dwSize', DWORD),
    ('byDefaultRoute', BYTE),
    ('byNetworkCardNum', BYTE),
    ('byWorkMode', BYTE),
    ('byRes', BYTE),
    ('struEtherNet', NET_DVR_ETHERNET_MULTI * 4),
    ('struManageHost1IpAddr', NET_DVR_IPADDR),
    ('struManageHost2IpAddr', NET_DVR_IPADDR),
    ('struAlarmHostIpAddr', NET_DVR_IPADDR),
    ('wManageHost1Port', WORD),
    ('wManageHost2Port', WORD),
    ('wAlarmHostIpPort', WORD),
    ('byIpResolver', BYTE * 64),
    ('wIpResolverPort', WORD),
    ('wDvrPort', WORD),
    ('wHttpPortNo', WORD),
    ('wDvrPort2', WORD),
    ('byRes2', BYTE * 4),
    ('struMulticastIpAddr', NET_DVR_IPADDR),
    ('struPPPoE', NET_DVR_PPPOECFG),
    ('byRes3', BYTE * 24),
])

NET_DVR_NETCFG_MULTI = struct_anon_15
LPNET_DVR_NETCFG_MULTI = POINTER(struct_anon_15)
