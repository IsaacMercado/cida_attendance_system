from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RECORD_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_RECORD_STATUS, [
    ('dwSize', DWORD),
    ('byRecUUID', BYTE * 64),
    ('byRecordStatus', BYTE),
    ('byRes1', BYTE * 3),
    ('dwRecordingTime', DWORD),
    ('byRes', BYTE * 596),
])

NET_DVR_RECORD_STATUS = struct_tagNET_DVR_RECORD_STATUS
LPNET_DVR_RECORD_STATUS = POINTER(struct_tagNET_DVR_RECORD_STATUS)
tagNET_DVR_RECORD_STATUS = struct_tagNET_DVR_RECORD_STATUS
