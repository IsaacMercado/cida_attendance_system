from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_WIRELESSDIAL_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_WIRELESSDIAL_STATUS, [
    ('dwSize', DWORD),
    ('byRealtimeMode', BYTE * 32),
    ('byUIMStatus', BYTE * 32),
    ('dwSignalQuality', DWORD),
    ('byDialStatus', BYTE * 32),
    ('struIpAddr', NET_DVR_IPADDR),
    ('struIPMask', NET_DVR_IPADDR),
    ('struGatewayIPMask', NET_DVR_IPADDR),
    ('struDnsServerIpAddr', NET_DVR_IPADDR),
    ('byRes', BYTE * 256),
])

NET_DVR_WIRELESSDIAL_STATUS = struct_tagNET_DVR_WIRELESSDIAL_STATUS
LPNET_DVR_WIRELESSDIAL_STATUS = POINTER(struct_tagNET_DVR_WIRELESSDIAL_STATUS)
tagNET_DVR_WIRELESSDIAL_STATUS = struct_tagNET_DVR_WIRELESSDIAL_STATUS
