from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .net_dvr_audio_steep_drop import NET_DVR_AUDIO_STEEP_DROP
from .net_dvr_handleexception_v40 import NET_DVR_HANDLEEXCEPTION_V40
from .net_vca_audio_abnormal import NET_VCA_AUDIO_ABNORMAL


class struct_tagNET_DVR_AUDIO_EXCEPTION(Structure):
    pass

_S(struct_tagNET_DVR_AUDIO_EXCEPTION, [
    ('dwSize', DWORD),
    ('byEnableAudioInException', BYTE),
    ('byRes1', BYTE * 3),
    ('struAudioAbnormal', NET_VCA_AUDIO_ABNORMAL),
    ('struAlarmSched', (NET_DVR_SCHEDTIME * 8) * 7),
    ('struHandleException', NET_DVR_HANDLEEXCEPTION_V40),
    ('dwMaxRelRecordChanNum', DWORD),
    ('dwRelRecordChanNum', DWORD),
    ('byRelRecordChan', DWORD * int((32 + 32))),
    ('struAudioSteepDrop', NET_DVR_AUDIO_STEEP_DROP),
    ('byRes2', BYTE * 24),
])

NET_DVR_AUDIO_EXCEPTION = struct_tagNET_DVR_AUDIO_EXCEPTION
LPNET_DVR_AUDIO_EXCEPTION = POINTER(struct_tagNET_DVR_AUDIO_EXCEPTION)
tagNET_DVR_AUDIO_EXCEPTION = struct_tagNET_DVR_AUDIO_EXCEPTION
