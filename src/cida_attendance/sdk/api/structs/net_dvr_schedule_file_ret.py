from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCHEDULE_FILE_RET(Structure):
    pass

_S(struct_tagNET_DVR_SCHEDULE_FILE_RET, [
    ('dwSize', DWORD),
    ('szFileName', c_char * 32),
    ('dwFileLen', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_SCHEDULE_FILE_RET = struct_tagNET_DVR_SCHEDULE_FILE_RET
LPNET_DVR_SCHEDULE_FILE_RET = POINTER(struct_tagNET_DVR_SCHEDULE_FILE_RET)
tagNET_DVR_SCHEDULE_FILE_RET = struct_tagNET_DVR_SCHEDULE_FILE_RET
