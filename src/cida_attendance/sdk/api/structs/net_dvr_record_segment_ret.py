from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RECORD_SEGMENT_RET_(Structure):
    pass

_S(struct_tagNET_DVR_RECORD_SEGMENT_RET_, [
    ('dwSize', DWORD),
    ('dwRecordTotalSize', DWORD),
    ('byRes', BYTE * 256),
])

NET_DVR_RECORD_SEGMENT_RET = struct_tagNET_DVR_RECORD_SEGMENT_RET_
LPNET_DVR_RECORD_SEGMENT_RET = POINTER(struct_tagNET_DVR_RECORD_SEGMENT_RET_)
tagNET_DVR_RECORD_SEGMENT_RET_ = struct_tagNET_DVR_RECORD_SEGMENT_RET_
