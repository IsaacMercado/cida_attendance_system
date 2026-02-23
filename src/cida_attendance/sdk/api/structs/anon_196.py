from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_196(Structure):
    pass

_S(struct_anon_196, [
    ('dwTotalLoginNum', DWORD),
    ('dwTotalRealPlayNum', DWORD),
    ('dwTotalPlayBackNum', DWORD),
    ('dwTotalAlarmChanNum', DWORD),
    ('dwTotalFormatNum', DWORD),
    ('dwTotalFileSearchNum', DWORD),
    ('dwTotalLogSearchNum', DWORD),
    ('dwTotalSerialNum', DWORD),
    ('dwTotalUpgradeNum', DWORD),
    ('dwTotalVoiceComNum', DWORD),
    ('dwTotalBroadCastNum', DWORD),
    ('dwTotalListenNum', DWORD),
    ('dwEmailTestNum', DWORD),
    ('dwBackupNum', DWORD),
    ('dwTotalInquestUploadNum', DWORD),
    ('dwRes', DWORD * 6),
])

NET_DVR_SDKSTATE = struct_anon_196
LPNET_DVR_SDKSTATE = POINTER(struct_anon_196)
