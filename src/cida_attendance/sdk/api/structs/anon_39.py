from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_37 import NET_DVR_RECORDSCHED
from .anon_38 import NET_DVR_RECORDDAY


class struct_anon_39(Structure):
    pass

_S(struct_anon_39, [
    ('dwSize', DWORD),
    ('dwRecord', DWORD),
    ('struRecAllDay', NET_DVR_RECORDDAY * 7),
    ('struRecordSched', (NET_DVR_RECORDSCHED * 8) * 7),
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
    ('byReserve', BYTE),
])

NET_DVR_RECORD_V30 = struct_anon_39
LPNET_DVR_RECORD_V30 = POINTER(struct_anon_39)
