from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_STREAM_RECORD_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_STREAM_RECORD_STATUS, [
    ('dwSize', DWORD),
    ('byRecord', BYTE),
    ('byOffLineRecord', BYTE),
    ('byRes1', BYTE * 2),
    ('dwRelatedHD', DWORD),
    ('byRes2', BYTE * 8),
])

NET_DVR_STREAM_RECORD_STATUS = struct_tagNET_DVR_STREAM_RECORD_STATUS
LPNET_DVR_STREAM_RECORD_STATUS = POINTER(struct_tagNET_DVR_STREAM_RECORD_STATUS)
tagNET_DVR_STREAM_RECORD_STATUS = struct_tagNET_DVR_STREAM_RECORD_STATUS
