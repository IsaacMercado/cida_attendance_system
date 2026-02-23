from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_anon_190(Structure):
    pass

_S(struct_anon_190, [
    ('sSerialNumber', BYTE * 48),
    ('byAlarmInPortNum', BYTE),
    ('byAlarmOutPortNum', BYTE),
    ('byDiskNum', BYTE),
    ('byDVRType', BYTE),
    ('byChanNum', BYTE),
    ('byStartChan', BYTE),
    ('byAudioChanNum', BYTE),
    ('byIPChanNum', BYTE),
    ('byZeroChanNum', BYTE),
    ('byMainProto', BYTE),
    ('bySubProto', BYTE),
    ('bySupport', BYTE),
    ('bySupport1', BYTE),
    ('bySupport2', BYTE),
    ('wDevType', WORD),
    ('bySupport3', BYTE),
    ('byMultiStreamProto', BYTE),
    ('byStartDChan', BYTE),
    ('byStartDTalkChan', BYTE),
    ('byHighDChanNum', BYTE),
    ('bySupport4', BYTE),
    ('byLanguageType', BYTE),
    ('byVoiceInChanNum', BYTE),
    ('byStartVoiceInChanNo', BYTE),
    ('bySupport5', BYTE),
    ('bySupport6', BYTE),
    ('byMirrorChanNum', BYTE),
    ('wStartMirrorChanNo', WORD),
    ('bySupport7', BYTE),
    ('byRes2', BYTE),
])

NET_DVR_DEVICEINFO_V30 = struct_anon_190
LPNET_DVR_DEVICEINFO_V30 = POINTER(struct_anon_190)
