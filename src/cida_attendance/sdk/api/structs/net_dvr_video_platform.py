from ctypes import Union

from ..base_classes import _S, BYTE
from .anon_331 import struct_anon_331
from .anon_332 import struct_anon_332


class union_tagNET_DVR_VIDEO_PLATFORM(Union):
    pass

_S(union_tagNET_DVR_VIDEO_PLATFORM, [
    ('byRes', BYTE * 160),
    ('struVideoPlatform', struct_anon_331),
    ('struNotVideoPlatform', struct_anon_332),
])

NET_DVR_VIDEO_PLATFORM = union_tagNET_DVR_VIDEO_PLATFORM
LPNET_DVR_VIDEO_PLATFORM = union_tagNET_DVR_VIDEO_PLATFORM
tagNET_DVR_VIDEO_PLATFORM = union_tagNET_DVR_VIDEO_PLATFORM
