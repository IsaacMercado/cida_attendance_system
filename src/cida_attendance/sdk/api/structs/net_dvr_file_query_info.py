from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, INT64
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FILE_QUERY_INFO(Structure):
    pass

_S(struct_tagNET_DVR_FILE_QUERY_INFO, [
    ('dwSize', DWORD),
    ('i64FileLen', INT64),
    ('byRes', BYTE * 256),
])

NET_DVR_FILE_QUERY_INFO = struct_tagNET_DVR_FILE_QUERY_INFO
LPNET_DVR_FILE_QUERY_INFO = POINTER(struct_tagNET_DVR_FILE_QUERY_INFO)
tagNET_DVR_FILE_QUERY_INFO = struct_tagNET_DVR_FILE_QUERY_INFO
