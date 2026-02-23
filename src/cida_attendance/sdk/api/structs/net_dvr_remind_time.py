from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_REMIND_TIME(Structure):
    pass

_S(struct_tagNET_DVR_REMIND_TIME, [
    ('byEnable', BYTE),
    ('byHour', BYTE),
    ('byMinute', BYTE),
    ('bySecond', BYTE),
])

NET_DVR_REMIND_TIME = struct_tagNET_DVR_REMIND_TIME
LPNET_DVR_REMIND_TIME = POINTER(struct_tagNET_DVR_REMIND_TIME)
tagNET_DVR_REMIND_TIME = struct_tagNET_DVR_REMIND_TIME
