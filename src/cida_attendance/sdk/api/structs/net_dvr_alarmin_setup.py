from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMIN_SETUP(Structure):
    pass

_S(struct_tagNET_DVR_ALARMIN_SETUP, [
    ('byAssiciateAlarmIn', BYTE * 512),
    ('byRes', BYTE * 100),
])

NET_DVR_ALARMIN_SETUP = struct_tagNET_DVR_ALARMIN_SETUP
LPNET_DVR_ALARMIN_SETUP = POINTER(struct_tagNET_DVR_ALARMIN_SETUP)
tagNET_DVR_ALARMIN_SETUP = struct_tagNET_DVR_ALARMIN_SETUP
