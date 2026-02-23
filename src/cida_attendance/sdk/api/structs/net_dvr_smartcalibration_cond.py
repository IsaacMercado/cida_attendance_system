from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SMARTCALIBRATION_COND(Structure):
    pass

_S(struct_tagNET_DVR_SMARTCALIBRATION_COND, [
    ('dwSize', DWORD),
    ('bySmartType', BYTE),
    ('byRes', BYTE * 3),
    ('dwChannel', DWORD),
    ('byRes1', BYTE * 128),
])

NET_DVR_SMARTCALIBRATION_COND = struct_tagNET_DVR_SMARTCALIBRATION_COND
LPNET_DVR_SMARTCALIBRATION_COND = POINTER(struct_tagNET_DVR_SMARTCALIBRATION_COND)
tagNET_DVR_SMARTCALIBRATION_COND = struct_tagNET_DVR_SMARTCALIBRATION_COND
