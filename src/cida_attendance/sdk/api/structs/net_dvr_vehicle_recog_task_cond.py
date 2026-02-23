from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VEHICLE_RECOG_TASK_COND(Structure):
    pass

_S(struct_tagNET_DVR_VEHICLE_RECOG_TASK_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('sDataIndex', c_char * 64),
    ('wTaskNo', WORD),
    ('byTask', BYTE),
    ('byRes1', BYTE),
    ('sDevDataIndex', c_char * 64),
    ('byRes', BYTE * 60),
])

NET_DVR_VEHICLE_RECOG_TASK_COND = struct_tagNET_DVR_VEHICLE_RECOG_TASK_COND
LPNET_DVR_VEHICLE_RECOG_TASK_COND = POINTER(struct_tagNET_DVR_VEHICLE_RECOG_TASK_COND)
tagNET_DVR_VEHICLE_RECOG_TASK_COND = struct_tagNET_DVR_VEHICLE_RECOG_TASK_COND
