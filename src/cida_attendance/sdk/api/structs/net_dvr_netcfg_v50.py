from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .anon_10 import NET_DVR_ETHERNET_V30
from .anon_12 import NET_DVR_PPPOECFG


class struct_tagNET_DVR_NETCFG_V50(Structure):
    pass

_S(struct_tagNET_DVR_NETCFG_V50, [
    ('dwSize', DWORD),
    ('struEtherNet', NET_DVR_ETHERNET_V30 * 2),
    ('struRes1', NET_DVR_IPADDR * 2),
    ('struAlarmHostIpAddr', NET_DVR_IPADDR),
    ('byRes2', BYTE * 4),
    ('wAlarmHostIpPort', WORD),
    ('byUseDhcp', BYTE),
    ('byIPv6Mode', BYTE),
    ('struDnsServer1IpAddr', NET_DVR_IPADDR),
    ('struDnsServer2IpAddr', NET_DVR_IPADDR),
    ('byIpResolver', BYTE * 64),
    ('wIpResolverPort', WORD),
    ('wHttpPortNo', WORD),
    ('struMulticastIpAddr', NET_DVR_IPADDR),
    ('struGatewayIpAddr', NET_DVR_IPADDR),
    ('struPPPoE', NET_DVR_PPPOECFG),
    ('byEnablePrivateMulticastDiscovery', BYTE),
    ('byEnableOnvifMulticastDiscovery', BYTE),
    ('wAlarmHost2IpPort', WORD),
    ('struAlarmHost2IpAddr', NET_DVR_IPADDR),
    ('byEnableDNS', BYTE),
    ('byRes', BYTE * 599),
])

NET_DVR_NETCFG_V50 = struct_tagNET_DVR_NETCFG_V50
LPNET_DVR_NETCFG_V50 = POINTER(struct_tagNET_DVR_NETCFG_V50)
tagNET_DVR_NETCFG_V50 = struct_tagNET_DVR_NETCFG_V50
