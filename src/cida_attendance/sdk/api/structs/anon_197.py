from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_197(Structure):
    pass

_S(struct_anon_197, [
    ('dwMaxLoginNum', DWORD),
    ('dwMaxRealPlayNum', DWORD),
    ('dwMaxPlayBackNum', DWORD),
    ('dwMaxAlarmChanNum', DWORD),
    ('dwMaxFormatNum', DWORD),
    ('dwMaxFileSearchNum', DWORD),
    ('dwMaxLogSearchNum', DWORD),
    ('dwMaxSerialNum', DWORD),
    ('dwMaxUpgradeNum', DWORD),
    ('dwMaxVoiceComNum', DWORD),
    ('dwMaxBroadCastNum', DWORD),
    ('dwRes', DWORD * 10),
])

NET_DVR_SDKABL = struct_anon_197
LPNET_DVR_SDKABL = POINTER(struct_anon_197)
