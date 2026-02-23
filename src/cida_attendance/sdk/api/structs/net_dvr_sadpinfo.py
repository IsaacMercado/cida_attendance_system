from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_SADPINFO(Structure):
    pass

_S(struct_tagNET_DVR_SADPINFO, [
    ('struIP', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('wFactoryType', WORD),
    ('chSoftwareVersion', c_char * 48),
    ('chSerialNo', c_char * 16),
    ('wEncCnt', WORD),
    ('byMACAddr', BYTE * 6),
    ('struSubDVRIPMask', NET_DVR_IPADDR),
    ('struGatewayIpAddr', NET_DVR_IPADDR),
    ('struDnsServer1IpAddr', NET_DVR_IPADDR),
    ('struDnsServer2IpAddr', NET_DVR_IPADDR),
    ('byDns', BYTE),
    ('byDhcp', BYTE),
    ('szGB28181DevID', BYTE * 32),
    ('byActivated', BYTE),
    ('byDeviceModel', BYTE * 24),
    ('byRes', BYTE * 101),
])

NET_DVR_SADPINFO = struct_tagNET_DVR_SADPINFO
LPNET_DVR_SADPINFO = POINTER(struct_tagNET_DVR_SADPINFO)
tagNET_DVR_SADPINFO = struct_tagNET_DVR_SADPINFO
