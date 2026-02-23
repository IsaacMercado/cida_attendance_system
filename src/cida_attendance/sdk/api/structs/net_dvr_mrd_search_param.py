from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_stream_info import NET_DVR_STREAM_INFO


class struct_tagNET_DVR_MRD_SEARCH_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_MRD_SEARCH_PARAM, [
    ('dwSize', DWORD),
    ('struStreamInfo', NET_DVR_STREAM_INFO),
    ('wYear', WORD),
    ('byMonth', BYTE),
    ('byDrawFrame', BYTE),
    ('byStreamType', BYTE),
    ('byLocalOrUTC', BYTE),
    ('byRes', BYTE * 30),
])

NET_DVR_MRD_SEARCH_PARAM = struct_tagNET_DVR_MRD_SEARCH_PARAM
LPNET_DVR_MRD_SEARCH_PARAM = POINTER(struct_tagNET_DVR_MRD_SEARCH_PARAM)
tagNET_DVR_MRD_SEARCH_PARAM = struct_tagNET_DVR_MRD_SEARCH_PARAM
