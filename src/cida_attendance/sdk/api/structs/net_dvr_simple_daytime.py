from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SIMPLE_DAYTIME(Structure):
    pass

_S(struct_tagNET_DVR_SIMPLE_DAYTIME, [
    ('byHour', BYTE),
    ('byMinute', BYTE),
    ('bySecond', BYTE),
    ('byRes', BYTE),
])

NET_DVR_SIMPLE_DAYTIME = struct_tagNET_DVR_SIMPLE_DAYTIME
LPNET_DVR_SIMPLE_DAYTIME = POINTER(struct_tagNET_DVR_SIMPLE_DAYTIME)
tagNET_DVR_SIMPLE_DAYTIME = struct_tagNET_DVR_SIMPLE_DAYTIME
