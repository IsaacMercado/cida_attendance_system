from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_WIFI_DHCP_ADDR_CFG(Structure):
    pass

_S(struct_tagNET_DVR_WIFI_DHCP_ADDR_CFG, [
    ('dwSize', DWORD),
    ('struStartAddr', NET_DVR_IPADDR),
    ('struEndAddr', NET_DVR_IPADDR),
    ('byRes', BYTE * 256),
])

NET_DVR_WIFI_DHCP_ADDR_CFG = struct_tagNET_DVR_WIFI_DHCP_ADDR_CFG
LPNET_DVR_WIFI_DHCP_ADDR_CFG = POINTER(struct_tagNET_DVR_WIFI_DHCP_ADDR_CFG)
tagNET_DVR_WIFI_DHCP_ADDR_CFG = struct_tagNET_DVR_WIFI_DHCP_ADDR_CFG
