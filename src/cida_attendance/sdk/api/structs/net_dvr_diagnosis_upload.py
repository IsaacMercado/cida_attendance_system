from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_DIAGNOSIS_UPLOAD(Structure):
    pass

_S(struct_tagNET_DVR_DIAGNOSIS_UPLOAD, [
    ('dwSize', DWORD),
    ('sStreamID', c_char * 32),
    ('sMonitorIP', c_char * 64),
    ('dwChanIndex', DWORD),
    ('dwWidth', DWORD),
    ('dwHeight', DWORD),
    ('struCheckTime', NET_DVR_TIME),
    ('byResult', BYTE),
    ('bySignalResult', BYTE),
    ('byBlurResult', BYTE),
    ('byLumaResult', BYTE),
    ('byChromaResult', BYTE),
    ('bySnowResult', BYTE),
    ('byStreakResult', BYTE),
    ('byFreezeResult', BYTE),
    ('byPTZResult', BYTE),
    ('byContrastResult', BYTE),
    ('byMonoResult', BYTE),
    ('byShakeResult', BYTE),
    ('sSNapShotURL', c_char * 256),
    ('byFlashResult', BYTE),
    ('byCoverResult', BYTE),
    ('bySceneResult', BYTE),
    ('byDarkResult', BYTE),
    ('byStreamType', BYTE),
    ('byRes2', BYTE * 59),
])

NET_DVR_DIAGNOSIS_UPLOAD = struct_tagNET_DVR_DIAGNOSIS_UPLOAD
LPNET_DVR_DIAGNOSIS_UPLOAD = POINTER(struct_tagNET_DVR_DIAGNOSIS_UPLOAD)
tagNET_DVR_DIAGNOSIS_UPLOAD = struct_tagNET_DVR_DIAGNOSIS_UPLOAD
