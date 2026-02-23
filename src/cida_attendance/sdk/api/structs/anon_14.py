from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_anon_14(Structure):
    pass

_S(struct_anon_14, [
    ('struDVRIP', NET_DVR_IPADDR),
    ('struDVRIPMask', NET_DVR_IPADDR),
    ('dwNetInterface', DWORD),
    ('byCardType', BYTE),
    ('byEnableDNS', BYTE),
    ('wMTU', WORD),
    ('byMACAddr', BYTE * 6),
    ('byEthernetPortNo', BYTE),
    ('bySilkScreen', BYTE),
    ('byUseDhcp', BYTE),
    ('byRes3', BYTE * 3),
    ('struGatewayIpAddr', NET_DVR_IPADDR),
    ('struDnsServer1IpAddr', NET_DVR_IPADDR),
    ('struDnsServer2IpAddr', NET_DVR_IPADDR),
])

NET_DVR_ETHERNET_MULTI = struct_anon_14
LPNET_DVR_ETHERNET_MULTI = POINTER(struct_anon_14)
