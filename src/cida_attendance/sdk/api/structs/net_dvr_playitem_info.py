from ctypes import Union

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .anon_461 import struct_anon_461
from .anon_462 import struct_anon_462
from .anon_463 import struct_anon_463


class union_tagNET_DVR_PLAYITEM_INFO(Union):
    pass

_S(union_tagNET_DVR_PLAYITEM_INFO, [
    ('struPlayItem', struct_anon_461),
    ('struPlaylistItem', struct_anon_462),
    ('struPlayPlanItem', struct_anon_463),
])

NET_DVR_PLAYITEM_INFO = union_tagNET_DVR_PLAYITEM_INFO
LPNET_DVR_PLAYITEM_INFO = POINTER(union_tagNET_DVR_PLAYITEM_INFO)
tagNET_DVR_PLAYITEM_INFO = union_tagNET_DVR_PLAYITEM_INFO
