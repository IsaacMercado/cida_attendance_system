from ctypes import Union

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_channel import NET_DVR_CHANNEL


class union_tagNET_DVR_SLAVE_CHANNEL_UNION(Union):
    pass

_S(union_tagNET_DVR_SLAVE_CHANNEL_UNION, [
    ('byRes', BYTE * 152),
    ('dwLocalChannel', DWORD),
    ('struRemoteChannel', NET_DVR_CHANNEL),
])

NET_DVR_SLAVE_CHANNEL_UNION = union_tagNET_DVR_SLAVE_CHANNEL_UNION
LPNET_DVR_SLAVE_CHANNEL_UNION = POINTER(union_tagNET_DVR_SLAVE_CHANNEL_UNION)
tagNET_DVR_SLAVE_CHANNEL_UNION = union_tagNET_DVR_SLAVE_CHANNEL_UNION
