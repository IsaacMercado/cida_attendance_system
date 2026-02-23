from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_UPLOAD_RECORD_INFO(Structure):
    pass

_S(struct_tagNET_DVR_UPLOAD_RECORD_INFO, [
    ('dwSize', DWORD),
    ('dwRecordType', DWORD),
    ('sCameraID', BYTE * 64),
    ('struStartTime', NET_DVR_TIME_EX),
    ('struStopTime', NET_DVR_TIME_EX),
    ('dwStoragePoolID', DWORD),
    ('byFormatType', BYTE),
    ('byVideoEncType', BYTE),
    ('byAudioEncType', BYTE),
    ('byISO8601', BYTE),
    ('cStartTimeDifferenceH', c_char),
    ('cStartTimeDifferenceM', c_char),
    ('cStopTimeDifferenceH', c_char),
    ('cStopTimeDifferenceM', c_char),
    ('byRes', BYTE * 120),
])

NET_DVR_UPLOAD_RECORD_INFO = struct_tagNET_DVR_UPLOAD_RECORD_INFO
LPNET_DVR_UPLOAD_RECORD_INFO = POINTER(struct_tagNET_DVR_UPLOAD_RECORD_INFO)
tagNET_DVR_UPLOAD_RECORD_INFO = struct_tagNET_DVR_UPLOAD_RECORD_INFO
