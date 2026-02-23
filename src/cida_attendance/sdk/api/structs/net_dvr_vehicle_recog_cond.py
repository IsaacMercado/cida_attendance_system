from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VEHICLE_RECOG_COND(Structure):
    pass

_S(struct_tagNET_DVR_VEHICLE_RECOG_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_VEHICLE_RECOG_COND = struct_tagNET_DVR_VEHICLE_RECOG_COND
LPNET_DVR_VEHICLE_RECOG_COND = POINTER(struct_tagNET_DVR_VEHICLE_RECOG_COND)
tagNET_DVR_VEHICLE_RECOG_COND = struct_tagNET_DVR_VEHICLE_RECOG_COND
