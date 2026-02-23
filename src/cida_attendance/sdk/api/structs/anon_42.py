from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_40 import NET_DVR_RECORDSCHED_V40
from .anon_41 import NET_DVR_RECORDDAY_V40


class struct_anon_42(Structure):
    pass

_S(struct_anon_42, [
    ('dwSize', DWORD),
    ('dwRecord', DWORD),
    ('struRecAllDay', NET_DVR_RECORDDAY_V40 * 7),
    ('struRecordSched', (NET_DVR_RECORDSCHED_V40 * 8) * 7),
    ('dwRecordTime', DWORD),
    ('dwPreRecordTime', DWORD),
    ('dwRecorderDuration', DWORD),
    ('byRedundancyRec', BYTE),
    ('byAudioRec', BYTE),
    ('byStreamType', BYTE),
    ('byPassbackRecord', BYTE),
    ('wLockDuration', WORD),
    ('byRecordBackup', BYTE),
    ('bySVCLevel', BYTE),
    ('byRecordManage', BYTE),
    ('byExtraSaveAudio', BYTE),
    ('byIntelligentRecord', BYTE),
    ('byRes', BYTE * 125),
])

NET_DVR_RECORD_V40 = struct_anon_42
LPNET_DVR_RECORD_V40 = POINTER(struct_anon_42)
