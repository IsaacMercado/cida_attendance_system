from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_wireless_security_cfg import NET_DVR_WIRELESS_SECURITY_CFG


class struct_tagNET_DVR_WIRELESSSERVER_FULLVERSION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_WIRELESSSERVER_FULLVERSION_CFG, [
    ('dwSize', DWORD),
    ('byWifiAPEnabled', BYTE),
    ('byBroadcastEnabled', BYTE),
    ('byWlanShareEnabled', BYTE),
    ('byDHCPEnabled', BYTE),
    ('bySSID', BYTE * 32),
    ('byRes1', BYTE * 11),
    ('byIPType', BYTE),
    ('struIPAddr', NET_DVR_IPADDR),
    ('struIPMask', NET_DVR_IPADDR),
    ('struGatewayIPMask', NET_DVR_IPADDR),
    ('struStartIPAddrPool', NET_DVR_IPADDR),
    ('struEndIPAddrPool', NET_DVR_IPADDR),
    ('struDNSServerIpAddr', NET_DVR_IPADDR * 2),
    ('struWirelessSecurityCfg', NET_DVR_WIRELESS_SECURITY_CFG),
    ('byRes', BYTE * 256),
])

NET_DVR_WIRELESSSERVER_FULLVERSION_CFG = struct_tagNET_DVR_WIRELESSSERVER_FULLVERSION_CFG
LPNET_DVR_WIRELESSSERVER_FULLVERSION_CFG = POINTER(struct_tagNET_DVR_WIRELESSSERVER_FULLVERSION_CFG)
tagNET_DVR_WIRELESSSERVER_FULLVERSION_CFG = struct_tagNET_DVR_WIRELESSSERVER_FULLVERSION_CFG
