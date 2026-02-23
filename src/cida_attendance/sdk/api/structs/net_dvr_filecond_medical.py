from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, LONG
from ..ctypes_preamble import POINTER
from .net_dvr_time_search_cond import NET_DVR_TIME_SEARCH_COND


class struct_tagNET_DVR_FILECOND_MEDICAL(Structure):
    pass

_S(struct_tagNET_DVR_FILECOND_MEDICAL, [
    ('lChannel', LONG),
    ('dwFileType', DWORD),
    ('dwIsLocked', DWORD),
    ('dwUseCardNo', DWORD),
    ('sCardNumber', BYTE * 32),
    ('struStartTime', NET_DVR_TIME_SEARCH_COND),
    ('struStopTime', NET_DVR_TIME_SEARCH_COND),
    ('szPatientID', c_char * 64),
    ('dwBigFileType', DWORD),
    ('byRes', BYTE * 252),
])

NET_DVR_FILECOND_MEDICAL = struct_tagNET_DVR_FILECOND_MEDICAL
LPNET_DVR_FILECOND_MEDICAL = POINTER(struct_tagNET_DVR_FILECOND_MEDICAL)
tagNET_DVR_FILECOND_MEDICAL = struct_tagNET_DVR_FILECOND_MEDICAL
