from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_416 import NET_DVR_POS_GENERIC
from .anon_417 import NET_DVR_POS_AVE
from .net_dvr_pos_nucleus import NET_DVR_POS_NUCLEUS


class union__NET_DVR_POS_PROTOCOL_UNION(Union):
    pass

_S(union__NET_DVR_POS_PROTOCOL_UNION, [
    ('byLenth', BYTE * 952),
    ('struGeneric', NET_DVR_POS_GENERIC),
    ('struAve', NET_DVR_POS_AVE),
    ('struNUCLEUS', NET_DVR_POS_NUCLEUS),
])

NET_DVR_POS_PROTOCOL_UNION = union__NET_DVR_POS_PROTOCOL_UNION
LPNET_DVR_POS_PROTOCOL_UNION = POINTER(union__NET_DVR_POS_PROTOCOL_UNION)
_NET_DVR_POS_PROTOCOL_UNION = union__NET_DVR_POS_PROTOCOL_UNION
