from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_START_FILE_TO_CLOUD_COND(Structure):
    pass

_S(struct_tagNET_DVR_START_FILE_TO_CLOUD_COND, [
    ('dwSize', DWORD),
    ('aCameraID', BYTE * 64),
    ('dwPoolID', DWORD),
    ('dwRepPoolID', DWORD),
    ('wReplication', WORD),
    ('byRes', BYTE * 178),
])

NET_DVR_START_FILE_TO_CLOUD_COND = struct_tagNET_DVR_START_FILE_TO_CLOUD_COND
LPNET_DVR_START_FILE_TO_CLOUD_COND = POINTER(struct_tagNET_DVR_START_FILE_TO_CLOUD_COND)
tagNET_DVR_START_FILE_TO_CLOUD_COND = struct_tagNET_DVR_START_FILE_TO_CLOUD_COND
