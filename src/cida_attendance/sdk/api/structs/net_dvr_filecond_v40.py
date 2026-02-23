from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, LONG
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .net_dvr_special_findinfo_union import NET_DVR_SPECIAL_FINDINFO_UNION


class struct_tagNET_DVR_FILECOND_V40(Structure):
    pass

_S(struct_tagNET_DVR_FILECOND_V40, [
    ('lChannel', LONG),
    ('dwFileType', DWORD),
    ('dwIsLocked', DWORD),
    ('dwUseCardNo', DWORD),
    ('sCardNumber', BYTE * 32),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
    ('byDrawFrame', BYTE),
    ('byFindType', BYTE),
    ('byQuickSearch', BYTE),
    ('bySpecialFindInfoType', BYTE),
    ('dwVolumeNum', DWORD),
    ('byWorkingDeviceGUID', BYTE * 16),
    ('uSpecialFindInfo', NET_DVR_SPECIAL_FINDINFO_UNION),
    ('byStreamType', BYTE),
    ('byAudioFile', BYTE),
    ('byRes2', BYTE * 30),
])

NET_DVR_FILECOND_V40 = struct_tagNET_DVR_FILECOND_V40
LPNET_DVR_FILECOND_V40 = POINTER(struct_tagNET_DVR_FILECOND_V40)
tagNET_DVR_FILECOND_V40 = struct_tagNET_DVR_FILECOND_V40
