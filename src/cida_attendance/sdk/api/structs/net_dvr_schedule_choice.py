from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCHEDULE_CHOICE(Structure):
    pass

_S(struct_tagNET_DVR_SCHEDULE_CHOICE, [
    ('byScheduleType', BYTE),
    ('byScheduleNo', BYTE),
    ('byRes', BYTE * 14),
])

NET_DVR_SCHEDULE_CHOICE = struct_tagNET_DVR_SCHEDULE_CHOICE
LPNET_DVR_SCHEDULE_CHOICE = POINTER(struct_tagNET_DVR_SCHEDULE_CHOICE)
tagNET_DVR_SCHEDULE_CHOICE = struct_tagNET_DVR_SCHEDULE_CHOICE
