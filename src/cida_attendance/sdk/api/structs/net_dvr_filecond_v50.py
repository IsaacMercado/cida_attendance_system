from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_special_findinfo_union import NET_DVR_SPECIAL_FINDINFO_UNION
from .net_dvr_stream_info import NET_DVR_STREAM_INFO
from .net_dvr_time_search_cond import NET_DVR_TIME_SEARCH_COND


class struct_tagNET_DVR_FILECOND_V50(Structure):
    pass

_S(struct_tagNET_DVR_FILECOND_V50, [
    ('struStreamID', NET_DVR_STREAM_INFO),
    ('struStartTime', NET_DVR_TIME_SEARCH_COND),
    ('struStopTime', NET_DVR_TIME_SEARCH_COND),
    ('byFindType', BYTE),
    ('byDrawFrame', BYTE),
    ('byQuickSearch', BYTE),
    ('byStreamType', BYTE),
    ('dwFileType', DWORD),
    ('dwVolumeNum', DWORD),
    ('byIsLocked', BYTE),
    ('byNeedCard', BYTE),
    ('byOnlyAudioFile', BYTE),
    ('bySpecialFindInfoType', BYTE),
    ('szCardNum', c_char * 32),
    ('szWorkingDeviceGUID', c_char * 16),
    ('uSpecialFindInfo', NET_DVR_SPECIAL_FINDINFO_UNION),
    ('dwTimeout', DWORD),
    ('byRes', BYTE * 252),
])

NET_DVR_FILECOND_V50 = struct_tagNET_DVR_FILECOND_V50
LPNET_DVR_FILECOND_V50 = POINTER(struct_tagNET_DVR_FILECOND_V50)
tagNET_DVR_FILECOND_V50 = struct_tagNET_DVR_FILECOND_V50
