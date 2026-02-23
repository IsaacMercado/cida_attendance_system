from ctypes import Union, c_char

from ..base_classes import _S
from ..ctypes_preamble import POINTER


class union_tagNET_DVR_IPADDR_UNION(Union):
    pass

_S(union_tagNET_DVR_IPADDR_UNION, [
    ('szIPv4', c_char * 16),
    ('szIPv6', c_char * 256),
])

NET_DVR_IPADDR_UNION = union_tagNET_DVR_IPADDR_UNION
LPNET_DVR_IPADDR_UNION = POINTER(union_tagNET_DVR_IPADDR_UNION)
tagNET_DVR_IPADDR_UNION = union_tagNET_DVR_IPADDR_UNION
