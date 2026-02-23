from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VEHICLERECOG_TASK_RESULT(Structure):
    pass

_S(struct_tagNET_DVR_VEHICLERECOG_TASK_RESULT, [
    ('dwSize', DWORD),
    ('sDevDataIndex', c_char * 64),
    ('byRes', BYTE * 256),
])

NET_DVR_VEHICLERECOG_TASK_RESULT = struct_tagNET_DVR_VEHICLERECOG_TASK_RESULT
LPNET_DVR_VEHICLERECOG_TASK_RESULT = POINTER(struct_tagNET_DVR_VEHICLERECOG_TASK_RESULT)
tagNET_DVR_VEHICLERECOG_TASK_RESULT = struct_tagNET_DVR_VEHICLERECOG_TASK_RESULT
