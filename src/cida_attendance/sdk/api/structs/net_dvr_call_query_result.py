from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CALL_QUERY_RESULT(Structure):
    pass

_S(struct_tagNET_DVR_CALL_QUERY_RESULT, [
    ('dwSize', DWORD),
    ('bySearchID', BYTE * 36),
    ('byStatus', BYTE),
    ('byRes', BYTE * 3),
    ('dwCount', DWORD),
    ('pResults', POINTER(BYTE)),
    ('byRes2', BYTE * 32),
])

NET_DVR_CALL_QUERY_RESULT = struct_tagNET_DVR_CALL_QUERY_RESULT
LPNET_DVR_CALL_QUERY_RESULT = POINTER(struct_tagNET_DVR_CALL_QUERY_RESULT)
tagNET_DVR_CALL_QUERY_RESULT = struct_tagNET_DVR_CALL_QUERY_RESULT
