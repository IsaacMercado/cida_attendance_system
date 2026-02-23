from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MRD_SEARCH_RESULT(Structure):
    pass

_S(struct_tagNET_DVR_MRD_SEARCH_RESULT, [
    ('dwSize', DWORD),
    ('byRecordDistribution', BYTE * 32),
    ('byHasEventRecode', BYTE * 31),
    ('byRes', BYTE),
])

NET_DVR_MRD_SEARCH_RESULT = struct_tagNET_DVR_MRD_SEARCH_RESULT
LPNET_DVR_MRD_SEARCH_RESULT = POINTER(struct_tagNET_DVR_MRD_SEARCH_RESULT)
tagNET_DVR_MRD_SEARCH_RESULT = struct_tagNET_DVR_MRD_SEARCH_RESULT
