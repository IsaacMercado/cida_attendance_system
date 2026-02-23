from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PPT_RESPONSE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_PPT_RESPONSE_PARAM, [
    ('byCurrentState', BYTE),
    ('byRes1', BYTE * 3),
    ('dwCurrentPage', DWORD),
    ('dwFileIndex', DWORD),
    ('dwTotalPageNum', DWORD),
    ('byRes2', BYTE * 16),
])

NET_DVR_PPT_RESPONSE_PARAM = struct_tagNET_DVR_PPT_RESPONSE_PARAM
LPNET_DVR_PPT_RESPONSE_PARAM = POINTER(struct_tagNET_DVR_PPT_RESPONSE_PARAM)
tagNET_DVR_PPT_RESPONSE_PARAM = struct_tagNET_DVR_PPT_RESPONSE_PARAM
