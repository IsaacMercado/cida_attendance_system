from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_audio_status import NET_DVR_AUDIO_STATUS
from .net_dvr_call_info import NET_DVR_CALL_INFO


class struct_tagNET_DVR_TERMINAL_CONFERENCE_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_TERMINAL_CONFERENCE_STATUS, [
    ('dwSize', DWORD),
    ('byConferenceState', BYTE),
    ('byConferenceType', BYTE),
    ('byDualStreamEnabled', BYTE),
    ('byMicPowerEnabled', BYTE),
    ('dwInputNo', DWORD),
    ('struCallInfo', NET_DVR_CALL_INFO),
    ('struAudioStatus', NET_DVR_AUDIO_STATUS),
    ('byRes2', BYTE * 32),
])

NET_DVR_TERMINAL_CONFERENCE_STATUS = struct_tagNET_DVR_TERMINAL_CONFERENCE_STATUS
LPNET_DVR_TERMINAL_CONFERENCE_STATUS = POINTER(struct_tagNET_DVR_TERMINAL_CONFERENCE_STATUS)
tagNET_DVR_TERMINAL_CONFERENCE_STATUS = struct_tagNET_DVR_TERMINAL_CONFERENCE_STATUS
