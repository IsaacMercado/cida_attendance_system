from ctypes import Union

from ..base_classes import _S, BYTE
from .net_dvr_ddns_address import NET_DVR_DDNS_ADDRESS
from .net_dvr_ip_address import NET_DVR_IP_ADDRESS


class union_anon_174(Union):
    pass

_S(union_anon_174, [
    ('byRes', BYTE * 200),
    ('struIpAddr', NET_DVR_IP_ADDRESS),
    ('struDdnsAddr', NET_DVR_DDNS_ADDRESS),
])

