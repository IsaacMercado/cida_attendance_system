from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_address import NET_DVR_ADDRESS
from .net_dvr_time_search import NET_DVR_TIME_SEARCH


class struct_tagNET_DVR_FINDDATA_V50(Structure):
    pass

_S(struct_tagNET_DVR_FINDDATA_V50, [
    ('sFileName', c_char * 100),
    ('struStartTime', NET_DVR_TIME_SEARCH),
    ('struStopTime', NET_DVR_TIME_SEARCH),
    ('struAddr', NET_DVR_ADDRESS),
    ('dwFileSize', DWORD),
    ('byLocked', BYTE),
    ('byFileType', BYTE),
    ('byQuickSearch', BYTE),
    ('byStreamType', BYTE),
    ('dwFileIndex', DWORD),
    ('sCardNum', c_char * 32),
    ('dwTotalLenH', DWORD),
    ('dwTotalLenL', DWORD),
    ('byBigFileType', BYTE),
    ('byRes', BYTE * 247),
])

NET_DVR_FINDDATA_V50 = struct_tagNET_DVR_FINDDATA_V50
LPNET_DVR_FINDDATA_V50 = POINTER(struct_tagNET_DVR_FINDDATA_V50)
tagNET_DVR_FINDDATA_V50 = struct_tagNET_DVR_FINDDATA_V50
